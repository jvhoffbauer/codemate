import * as vscode from 'vscode';
import { Suggestion, Example } from './ApiBindings';
import {sprightly} from "sprightly"
import { Eta } from "eta"


// A webview panel to show code suggestions
let panel: vscode.WebviewPanel | undefined;
// The template engine to render the webview
let eta: Eta | undefined;



function createWebview(context: vscode.ExtensionContext) {

    // Create a new panel where we can show code suggestions
	panel = vscode.window.createWebviewPanel(
        'codemateWindow',
        'CodeMate',
        vscode.ViewColumn.Two,
        { retainContextWhenHidden: true, enableScripts: true }
    );

    // Create the template engine
    eta = new Eta({ views: context.asAbsolutePath('src/templates') })

    // Render the webview with the welcome message
    const html = eta.render("view_welcome", {});
    panel.webview.html = html;
}

function updateWebview(suggestion: Suggestion) {
    if (!panel || !eta) {
        return;
    }

    // Render the webview with the new suggestion
    const html = eta.render("view_examples", {suggestion: suggestion});
    panel.webview.html = html;
}

export { createWebview, updateWebview};