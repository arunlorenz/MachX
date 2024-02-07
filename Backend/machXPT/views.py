from django.shortcuts import render
from django.http import JsonResponse

def generate_answer(code_snippet, doubt):
    
    try:
        if code_snippet == "":
            query = doubt
        else:
            query = f"code:\n{code_snippet}\nmy question: {doubt}"
        
        import google.generativeai as genai
    
        gemini_api_key = "AIzaSyCUPunF3tHK7JTnpIxIBC630uTddIqKzCY"
        genai.configure(api_key = gemini_api_key)
        
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(query)
                    
        return response.text
    
    except Exception as e:
        return "Oops! Some error occured please try again!"

def ask_mach(request):
    return render(request, "machXPT.html")

def submit_form(request):
    if request.method == 'POST':
        # Get code snippet and doubt from POST data
        code_snippet = request.POST.get('code_snippet', '')
        doubt = request.POST.get('doubt', '')
        
        # Process the code snippet and doubt to generate the answer
        answer = generate_answer(code_snippet, doubt)  # You need to implement this function
        
        # Return the answer as JSON response
        return JsonResponse({'answer': answer})
    else:
        return JsonResponse({'error': 'Invalid request method'})