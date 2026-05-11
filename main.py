from groq import generate_response
def reinforce():
    print("\n=====Reinforcement Learning=====")
    prompt=input("Enter the prompt: ").strip()
    if not prompt:
        print("Prompt required")
    res=generate_response(prompt,temperature=0.3,max_tokens=1024)
    print(f"Initial : {res}")
    try:
        rating=int(input("Enter the rating 1- 5: "))
        rating=rating if 1<=rating<=5 else 3
    except:
        rating=3
    feedback=input("Feedback: ").strip()
    prompt=feedback+prompt
    res1=generate_response(feedback,temperature=0.3,max_tokens=1024)
    print(f"\nImproved : {res1} (Feedback : {feedback})")

def role_based():
    print("\n=====Role Based Prompting =====")
    prompt=input("Enter the prompt: ").strip()
    role=int(input("Enter 1 for Teacher 2 for Engineer 3.Expert "))
    if not prompt:
        print("Prompt required")
    if role==1:
        prompt="Your role is a teacher ."+prompt
    if role==2:
        prompt="Your role is a Engineer ."+prompt
    if role==3:
        prompt="Your role is a Expert ."+prompt
    res=generate_response(prompt,temperature=0.3,max_tokens=1024)
    print(f"Initial : {res}")
reinforce()
role_based()