import * as vscode from 'vscode';
import fetchData, { Example, Suggestion } from './ApiBindings';
import { createWebview, updateWebview } from './Panel';


export function activate(context: vscode.ExtensionContext) {
    /**
     * Activate the extension by registering all commands and event handlers.
     * @param context The extension context.
     */

    // Show a cool message when the extension is activated with emojis
	console.log('Activating codemate extension 🚀');
    vscode.window.showInformationMessage("Codemate is active! 🚀");

	// Track cursor position
    context.subscriptions.push(vscode.window.onDidChangeTextEditorSelection(updateCursorPosition));

    // Register a command to show the status info
	context.subscriptions.push(vscode.commands.registerCommand('codemate-extension.showStatusInfo', () => {
        // For now, just show a message
		vscode.window.showInformationMessage("Codemate is active! 🚀");
	}));

    // Create the webview
    createWebview(context);
}

async function updateCursorPosition() {
    const editor = vscode.window.activeTextEditor;

    if (editor) {
        const position = editor.selection.active;
        const document = editor.document;

        const suggestion = await fetchData(document.getText(), position.line, position.character);

		// panel.webview.html = getWebviewContent(event.context);

        // Send a message to the webview
        updateWebview(suggestion);
    }
}




// This method is called when your extension is deactivated
export function deactivate() {}
