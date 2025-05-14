import random

# Store user's name
user_name = ""

# GREETING
def greet():
    greetings = ["Hi there!", "Hello!", "Hey! How can I help you?", "Greetings!"]
    return random.choice(greetings)

def ask_name():
    global user_name
    if not user_name:
        user_name = input("ChatBot: What's your name? ")
    return f"ChatBot: Hello, {user_name}!"

# JOKES
def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the computer go to therapy? It had too many bytes of trauma.",
        "Why did the Python programmer go broke? Because he couldn't C#!"
    ]
    return random.choice(jokes)

# STUDENT QUESTIONS
def student_faq_response(user_input):
    user_input = user_input.lower()
    if "favorite subject" in user_input:
        return "ChatBot: My favorite subject is Data Science. How about you?"
    elif "help me with my homework" in user_input:
        return "ChatBot: Sure! What subject or question do you need help with?"
    elif "latest trends in education" in user_input:
        return "ChatBot: Some of the latest trends include online learning, flipped classrooms, and personalized learning using AI."
    elif "study tips" in user_input:
        return "ChatBot: A great study tip is to break your study sessions into intervals (Pomodoro technique)."
    elif "best time to study" in user_input:
        return "ChatBot: The best time to study is when you're most alert—often in the morning."
    elif "explain this concept" in user_input:
        return "ChatBot: Sure! Could you please specify the concept you'd like me to explain?"
    elif "good resources for learning" in user_input:
        return "ChatBot: Codecademy, freeCodeCamp, Khan Academy, and YouTube are great for learning!"
    elif "how to prepare for exams" in user_input:
        return "ChatBot: Review notes, create a schedule, solve past papers, and take breaks!"
    elif "meaning of life" in user_input:
        return "ChatBot: The meaning of life differs for everyone. Some say it's 42 😉."
    elif "study routine" in user_input:
        return "ChatBot: Try studying 25 mins, then a 5-minute break (Pomodoro)."
    elif "thoughts on online education" in user_input:
        return "ChatBot: It’s flexible but needs discipline and motivation."
    elif "manage stress while studying" in user_input:
        return "ChatBot: Exercise, good sleep, breaks, and deep breathing can help reduce stress."
    return None

# CODING QUESTIONS
def coding_response(user_input):
    user_input = user_input.lower()

    if "class in java" in user_input:
        return """ChatBot: In Java, a class is a blueprint for objects:
```java
public class Car {
    String color;
    int speed;

    void drive() {
        System.out.println("Driving the car");
    }
}
```"""
    elif "inheritance in java" in user_input:
        return """ChatBot: Inheritance allows one class to inherit another:
```java
class Animal {
    void eat() {
        System.out.println("Eating...");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Barking...");
    }
}
```"""
    elif "class in python " in user_input:
        return """ChatBot: A class in Python example:
```python
class Car:
    def __init__(self, color):
        self.color = color

    def drive(self):
        print("Driving a", self.color, "car")
```"""
    elif "inheritance in python" in user_input:
        return """ChatBot: Inheritance in Python:
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
```"""
    elif "polymorphism " in user_input:
        return """ChatBot: Polymorphism allows same method names with different behavior:
```python
class Bird:
    def sound(self):
        print("Tweet")

class Duck(Bird):
    def sound(self):
        print("Quack")

def make_sound(bird):
    bird.sound()

make_sound(Bird())
make_sound(Duck())
```"""
    elif "encapsulation " in user_input:
        return """ChatBot: Encapsulation in Java is Encapsulation means binding data and code together and restricting direct access to some of the object's components.
It helps protect the data and ensures that it's used in the correct way.:
```java
public class Student {
    private String name;

    public void setName(String n) {
        name = n;
    }

    public String getName() {
        return name;
    }
}
```"""
    elif "abstraction " in user_input:
        return """ChatBot: Abstraction hides implementation details:
```java
abstract class Shape {
    abstract void draw();
}

class Circle extends Shape {
    void draw() {
        System.out.println("Drawing a circle");
    }
}
```"""
    elif "python loop" in user_input:
        return """ChatBot: Python loop example:
```python
for i in range(5):
    print("Count:", i)
```"""
    elif "java loop" in user_input:
        return """ChatBot: Java loop example:
```java
for (int i = 0; i < 5; i++) {
    System.out.println("Count: " + i);
}
```"""
    return None

# CHATBOT CORE LOGIC
def chat_response(user_input):
    global user_name
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        if not user_name:
            return ask_name()
        return f"ChatBot: {greet()}"

    elif "joke" in user_input:
        return f"ChatBot: {tell_joke()}"

    coding_ans = coding_response(user_input)
    if coding_ans:
        return coding_ans

    student_ans = student_faq_response(user_input)
    if student_ans:
        return student_ans

    elif "bye" in user_input:
        return f"ChatBot: {farewell()}"

    return "ChatBot: Sorry, I didn't quite catch that. Try asking something else!"

# GOODBYE
def farewell():
    goodbyes = ["Goodbye! Have a great day!", "See you later!", "Take care!", "Bye!"]
    return random.choice(goodbyes)

# RUNNING THE CHATBOT
def run_chatbot():
    print("ChatBot: Hello! I'm your improved chatbot.")
    print("ChatBot: Type 'bye' to terminate the chat.")
    while True:
        user_input = input("You: ")
        response = chat_response(user_input)
        if response is None or "bye" in user_input.lower():
            break
        print(response)

# Start
run_chatbot()
