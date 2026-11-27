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
PAGE = """<!doctype html>
<html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Message Classifier</title>
<style>
body{font-family:system-ui,sans-serif;background:#f5f6fa;margin:0;padding:24px}
.card{max-width:640px;margin:auto;background:#fff;padding:24px;
border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,.08)}
h2{margin-top:0}
textarea{width:100%;height:110px;padding:10px;border:1px solid #ccd;
border-radius:8px;box-sizing:border-box;font-size:15px}
button{background:#2563eb;color:#fff;border:0;padding:10px 20px;
border-radius:8px;font-size:15px;cursor:pointer;margin-top:10px}
.ex{background:#e8ecf5;color:#333;padding:6px 12px;font-size:13px;
margin-right:6px}
.badge{display:inline-block;padding:4px 12px;border-radius:99px;
color:#fff;font-weight:600;margin-top:16px}
.order{background:#16a34a}.question{background:#2563eb}
.complaint{background:#dc2626}.other{background:#6b7280}
#reply{background:#f0f4ff;padding:14px;border-radius:8px;margin-top:10px}
</style></head>
<body><div class="card">
<h2>Customer Message Classifier</h2>
<p>Paste a customer message. The app classifies it and drafts a reply.</p>
<button class="ex" onclick="ex('Hi, I want to order 3 shirts.')">Order</button>
<button class="ex" onclick="ex('How much is shipping to Lahore?')">Question</button>
<button class="ex" onclick="ex('My package is late and I want a refund.')">Complaint</button>
<textarea id="t" placeholder="Paste a customer message..."></textarea>
<button onclick="go()">Classify</button>
<div id="out"></div>
<script>
function ex(s){document.getElementById('t').value=s;go();}
async function go(){
  const r = await fetch('/classify', {method:'POST',
    headers:{'Content-Type':'application/json'},
    body: JSON.stringify({text: document.getElementById('t').value})});
  const d = await r.json();
  const out = document.getElementById('out');
  out.innerHTML = '<span class="badge"></span><div id="reply"></div>';
  out.querySelector('.badge').textContent = d.category;
  out.querySelector('.badge').classList.add(d.category);
  document.getElementById('reply').textContent = d.draft_reply;
}
</script></div></body></html>"""