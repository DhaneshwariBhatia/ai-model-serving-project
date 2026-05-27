import { useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {

  const [task, setTask] = useState('sentiment')
  const [text, setText] = useState('')
  const [question, setQuestion] = useState('')
  const [context, setContext] = useState('')
  const [result, setResult] = useState('')
  const [loading, setLoading] = useState(false)

  const API_URL = 'http://127.0.0.1:8000'

  const handleSubmit = async () => {

    setLoading(true)
    setResult('')

    try {

      let response

      if (task === 'sentiment') {

        response = await axios.post(`${API_URL}/sentiment`, {
          text,
        })

      }

      else if (task === 'generate') {

        response = await axios.post(`${API_URL}/generate`, {
          text,
        })

      }

      else if (task === 'translate') {

        response = await axios.post(`${API_URL}/translate`, {
          text,
        })

      }

      else if (task === 'grammar') {

        response = await axios.post(`${API_URL}/grammar`, {
          text,
        })

      }

      else if (task === 'qa') {

        response = await axios.post(`${API_URL}/qa`, {
          question,
          context,
        })

      }

      if(task === 'sentiment'){

  setResult(response.data.prediction[0].label)

}

else if(task === 'generate'){

  setResult(response.data.output)

}

else if(task === 'translate'){

  setResult(
    response.data.translated_text[0].translation_text
  )

}

else if(task === 'grammar'){

  setResult(
    response.data.corrected_text[0].generated_text
  )

}

else if(task === 'qa'){

  setResult(response.data.answer.answer)

}

    }

    catch (error) {

      setResult('Error connecting to backend')

    }

    setLoading(false)

  }

  return (

    <div className="app">

      <div className="overlay"></div>

      <div className="container">

        <h1>Model Serving Using AI</h1>

        <p className="subtitle">
          FastAPI + Hugging Face + React + Vite
        </p>

        <div className="card">

          <label>Select AI Task</label>

          <select
            value={task}
            onChange={(e) => setTask(e.target.value)}
          >

            <option value="sentiment">
              Sentiment Analysis
            </option>

            <option value="generate">
              Text Generation
            </option>

            <option value="translate">
              Translation
            </option>

            <option value="grammar">
              Grammar Correction
            </option>

            <option value="qa">
              Question Answering
            </option>

          </select>

          {
            task === 'qa' ? (

              <>

                <textarea
                  placeholder="Enter Question"
                  value={question}
                  onChange={(e) => setQuestion(e.target.value)}
                />

                <textarea
                  placeholder="Enter Context Paragraph"
                  value={context}
                  onChange={(e) => setContext(e.target.value)}
                />

              </>

            ) : (

              <textarea
                placeholder="Enter your text here..."
                value={text}
                onChange={(e) => setText(e.target.value)}
              />

            )
          }

          <button onClick={handleSubmit}>

            {
              loading
                ? 'Generating...'
                : 'Generate Response'
            }

          </button>

        </div>

        <div className="result-box">

          <h2>AI Response</h2>

          <pre>{result}</pre>

        </div>

      </div>

    </div>

  )
}

export default App