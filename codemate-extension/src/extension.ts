// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';

let panel: vscode.WebviewPanel | undefined;


// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "codemate-extension" is now active!');

	// Track cursor position
    context.subscriptions.push(vscode.window.onDidChangeTextEditorSelection(updateCursorPosition))

	context.subscriptions.push(vscode.commands.registerCommand('codemate-extension.helloWorld', () => {
		// The code you place here will be executed every time your command is executed
		// Display a message box to the user
		vscode.window.showInformationMessage("test3")
	}));

	if (panel) {
		panel.webview.html = getWebviewContent();
	}
	
}

const NUM_CONTEXT_LINES = 4

async function updateCursorPosition(event: any) {
    const editor = vscode.window.activeTextEditor;

    if (editor) {
        const position = editor.selection.active;
        const line = editor.document.lineAt(position.line).text;
        const document = editor.document;

        const contextLines = [];
        for (let i = Math.max(0, position.line - NUM_CONTEXT_LINES); i <= Math.min(document.lineCount - 1, position.line + NUM_CONTEXT_LINES); i++) {
            contextLines.push(document.lineAt(i).text);
        }

        let context = contextLines.join('\n')

        console.log(context)
        const code = await fetchData(context);
        console.log(code)

		if (!panel) {
            panel = vscode.window.createWebviewPanel(
                'cursorPositionTracker',
                'Cursor Position Tracker',
                vscode.ViewColumn.Two,
                { retainContextWhenHidden: true, enableScripts: true }
            );

            panel.webview.html = getWebviewContent();
        }

        // Send a message to the webview
        panel.webview.postMessage({context: code});
    }
}

async function fetchData(context: string) {
    const url = 'http://127.0.0.1:8080/suggestion';

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ context }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data: any = await response.json();
        return data.code;
    } catch (error) {
        console.error('Error fetching data:', error);
        return ''; // Return an empty string or handle the error as needed
    }
}

function getWebviewContent() {
    return `
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    padding: 20px;
                    whiteSpace: 'pre';
                }
                code {
                    display: block;
                    white-space: pre-wrap   
                  }
            </style>
            <script>
                const vscode = acquireVsCodeApi();

                window.addEventListener('message', event => {
                    const message = event.data;
                    document.getElementById('context').innerText = message.context;
                });
            </script>
        </head>
        <body>
            <h2>Context</h2>
            <p><code id="context"></code></p>
        </body>
        </html>
    `;
}

// This method is called when your extension is deactivated
export function deactivate() {}
