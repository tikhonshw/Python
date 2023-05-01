const apiKey = 'YOUR_API_KEY';
const prompt = 'Hello, world!';

fetch('https://api.openai.com/v1/engines/davinci-codex/completions', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${apiKey}`,
  },
  body: JSON.stringify({
    'prompt': prompt,
    'max_tokens': 5,
    'n': 1,
    'stop': '.'
  })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error(error));