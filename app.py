from fastapi import FastAPI
from pydantic import BaseModel
from classifier import classify

app = FastAPI(title="Message Classifier")


class Message(BaseModel):
    text: str


@app.post("/classify")
def classify_message(msg: Message):
    return classify(msg.text)
from fastapi.responses import HTMLResponse

PAGE = """<!doctype html>
<html><head><meta charset="utf-8"><title>Message Classifier</title>
<style>
body{font-family:sans-serif;max-width:600px;margin:40px auto;padding:0 16px}
textarea{width:100%;height:120px}
button{padding:8px 16px;margin-top:8px}
pre{background:#f4f4f4;padding:12px;white-space:pre-wrap}
</style></head>
<body>
<h2>Customer Message Classifier</h2>
<textarea id="t" placeholder="Paste a customer message..."></textarea><br>
<button onclick="go()">Classify</button>
<pre id="out"></pre>
<script>
async function go(){
  const r = await fetch('/classify', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({text: document.getElementById('t').value})
  });
  const d = await r.json();
  document.getElementById('out').textContent = JSON.stringify(d, null, 2);
}
</script>
</body></html>"""


@app.get("/", response_class=HTMLResponse)
def home():
    return PAGE