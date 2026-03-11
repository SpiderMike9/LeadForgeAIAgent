import os
from flask import Flask, request, jsonify
import google.generativeai as genai

# This makes the cloud robot listen for messages
app = Flask(__name__)

# Configure Sarah's Brain
genai.configure(api_key='AIzaSyDmYcB_O8nTfeP-Ia_rnghS_HnzH0LubDk')
model = genai.GenerativeModel('gemini-1.5-flash')

system_prompt = """
You are Sarah, the friendly virtual receptionist for Raleigh Realty Pros. 
Greet callers warmly, answer questions about listings, schedule viewings, 
and capture leads (Name/Email/Phone). 
UPSELL: 'Would you like our free market report?'
"""

@app.route("/", methods=["POST"])
def sarah_chat():
    # This part takes the voice text coming from your website
    data = request.get_json()
    user_text = data.get("text", "")
    
    # Sarah thinks and generates a response
    response = model.generate_content(system_prompt + "\nUser: " + user_text)
    
    # Send the answer back to the website
    return jsonify({"response": response.text})

if __name__ == "__main__":
    # This tells the cloud which port to use

    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
