const BASE_API_URL =  'http://127.0.0.1:8080';


interface SuggestionRequest {
    text: string;
    line: number;
    column: number;
}

interface Example {
    text: string;
    source: string;
    stars: number;
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

    console.log(JSON.stringify(payload));

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