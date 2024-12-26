<h1 align="center">Mood-Based Food Recommendation App</h1>
<p align="center">Discover delicious recipes tailored to your mood with the power of <strong>Groq API</strong>!</p>

<hr>

<h2>Features</h2>
<ul>
  <li>Input your mood and get personalized food recommendations.</li>
  <li>Food recommendations include links to recipes on <a href="https://www.allrecipes.com/">AllRecipes</a>.</li>
  <li>Emojis are added to the food recommendations for a fun touch!</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>Python 3.7 or later</li>
  <li>Modules to install:
    <ul>
      <li><code>Flask</code></li>
      <li><code>requests</code></li>
      <li><code>groq</code></li>
      <li><code>python-dotenv</code></li>
    </ul>
  </li>
</ul>

<h2>Setup Instructions</h2>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/your-username/mood-food-recommendation.git</code></pre>
  </li>
  <li>Navigate to the project folder:
    <pre><code>cd mood-food-recommendation</code></pre>
  </li>
  <li>Create a virtual environment (optional but recommended):
    <pre><code>python -m venv venv</code></pre>
    <p>Activate the virtual environment:</p>
    <ul>
      <li>On Windows:
        <pre><code>venv\Scripts\activate</code></pre>
      </li>
      <li>On macOS/Linux:
        <pre><code>source venv/bin/activate</code></pre>
      </li>
    </ul>
  </li>
  <li>Install required modules:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Create a <code>.env</code> file in the root directory and add your Groq API key:
    <pre><code>GROQ_API_KEY=your_api_key_here</code></pre>
  </li>
</ol>

<h2>Usage</h2>
<ol>
  <li>Run the Flask app:
    <pre><code>python app.py</code></pre>
  </li>
  <li>Access the app in your browser at <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a>.</li>
  <li>Enter your mood in the input field, and the app will recommend food based on your mood!</li>
</ol>

<h2>Contributing</h2>
<p>Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request with your improvements or fixes.</p>

<h2>Contact</h2>
<p>For questions or feedback, please reach out via the repository or open an issue.</p>
