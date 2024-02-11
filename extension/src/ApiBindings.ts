// TODO: This should be configurable when deploying the extension, 
// so that the extension can be used with different backends.
const BASE_API_URL =  'http://127.0.0.1:8080';


interface SuggestionRequest {
    text: string;
    line: number;
    column: number;
}

interface Example {
    text: string;
    source: string;
}

interface Suggestion {
    examples: Example[];
}


async function fetchData(context: string, line: number, column: number) {
    const url = `${BASE_API_URL}/suggestion`;

    const payload: SuggestionRequest = {
        text: context,
        line: line,
        column: column
    };

    try {
        // Make the request
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        });

        // Ensure we got an OK response
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse the response body as JSON
        const data: any = await response.json() as Suggestion;
        return data;
    } catch (error) {
        console.error(error);
        return null;
    }
}

export default fetchData;
export { Suggestion, Example };