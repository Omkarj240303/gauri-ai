import { useState } from "react";
import "./index.css";

const API = "";

const suggestions = [
  "What SAP capabilities does Gauri have?",
  "What Salesforce services does Gauri provide?",
  "What is Gauri's office location?",
  "What are Gauri's security and VPN requirements?"
];

function App() {
  const [messages, setMessages] = useState([]);
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);

  async function sendMessage(text = query) {
    if (!text.trim() || loading) return;

    const question = text.trim();
    setQuery("");

    setMessages((prev) => [
      ...prev,
      { role: "user", text: question }
    ]);

    setLoading(true);

    try {
      const response = await fetch(`${API}/api/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ query: question })
      });

      if (!response.ok) {
        throw new Error();
      }

      const data = await response.json();

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: data.answer,
          grounding: data.grounding,
          sources: [...new Set(data.sources || [])]
        }
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "Unable to connect to the Gauri AI server."
        }
      ]);
    } finally {
      setLoading(false);
    }
  }

  function newChat() {
    setMessages([]);
    setQuery("");
  }

  function handleKeyDown(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  }

  return (
    <div className="app">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-logo">G</div>
          <div>
            <h2>GAURI</h2>
            <span>AI Assistant</span>
          </div>
        </div>

        <button className="new-chat" onClick={newChat}>
          <span>＋</span>
          New chat
        </button>

        <div className="sidebar-section">
          <span>ABOUT</span>
          <p>Intelligent assistant for Gauri company information, services and policies.</p>
        </div>

        <div className="sidebar-bottom">
          <div className="status-dot"></div>
          <div>
            <strong>AI Assistant</strong>
            <small>System online</small>
          </div>
        </div>
      </aside>

      <section className="main">
        <header className="topbar">
          <div>
            <h1>Gauri AI Assistant</h1>
            <span>Enterprise knowledge assistant</span>
          </div>

          <div className="online">
            <span></span>
            Online
          </div>
        </header>

        <main className="chat">
          {!messages.length ? (
            <div className="welcome">
              <div className="welcome-icon">G</div>

              <h2>How can I help you?</h2>

              <p>
                Ask me about Gauri's services, technologies,
                company information and internal policies.
              </p>

              <div className="suggestions">
                {suggestions.map((item) => (
                  <button
                    key={item}
                    onClick={() => sendMessage(item)}
                  >
                    {item}
                  </button>
                ))}
              </div>
            </div>
          ) : (
            <div className="messages">
              {messages.map((message, index) => (
                <div
                  key={index}
                  className={`message ${message.role}`}
                >
                  <div className="avatar">
                    {message.role === "user" ? "You" : "G"}
                  </div>

                  <div className="message-content">
                    <div className="message-name">
                      {message.role === "user"
                        ? "You"
                        : "Gauri AI"}
                    </div>

                    <div className="bubble">
                      {message.text}
                    </div>

                    {message.grounding && (
                      <div className="grounding">
                        <span>✓</span>
                        Grounded answer
                      </div>
                    )}

                    {message.sources?.length > 0 && (
                      <div className="sources">
                        <div className="sources-title">
                          Sources
                        </div>

                        {message.sources.map((source, i) => (
                          <div className="source" key={i}>
                            <span>◈</span>
                            {source}
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                </div>
              ))}

              {loading && (
                <div className="message assistant">
                  <div className="avatar">G</div>

                  <div className="message-content">
                    <div className="message-name">
                      Gauri AI
                    </div>

                    <div className="bubble typing">
                      <span></span>
                      <span></span>
                      <span></span>
                    </div>
                  </div>
                </div>
              )}
            </div>
          )}
        </main>

        <div className="composer">
          <div className="composer-box">
            <textarea
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Ask Gauri AI anything..."
              rows="1"
            />

            <button
              className="send"
              onClick={() => sendMessage()}
              disabled={loading || !query.trim()}
            >
              ↑
            </button>
          </div>

          <p>
            Gauri AI can make mistakes. Verify important information.
          </p>
        </div>
      </section>
    </div>
  );
}

export default App;