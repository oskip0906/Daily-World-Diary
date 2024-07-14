# How to Generate a New Diary

1. **Log In to OpenAI Platform:**
   - Visit the [OpenAI Platform](https://platform.openai.com/) and acquire a ChatGPT API key.
     
2. **Set Up Environment Variables:**

   - Create a file named `.env` in the `main_functions` folder with the following lines:
  
     ```env
     secret_api_key = 'YOUR_CHATGPT_API_KEY'
     chatgpt_model = 'YOUR_DESIRED_CHATGPT_MODEL'
     ```
     
3. **Run the Diary Generation Script:**
   - Navigate to the Python file named `generate_diary.py` and execute the program. 
   
4. **Locate Your New Diary:**
   - The newly generated diary will be saved as a text file with today's date as its name in the `daily_diaries` folder.
   - Launch the webpage at `index.html` to view it. 
