![Screenshot 2024-09-09 at 10 33 24 PM](https://github.com/user-attachments/assets/8a53d090-5a73-4bc0-be11-4935a7fc194d)![Uploading Screenshot 2024-09-09 at 10.36.50 PM.png…]()
<img width="1327" alt="Screenshot 2024-09-09 at 10 37 01 PM" src="https://github.com/user-attachments/assets/a19127ea-c6d2-4602-a30d-cf7fa998c4bf">


**Inspiration**

Members of our group have long grappled with maintaining their health and achieving their dietary goals amidst busy schedules and priorities. Whether juggling the demands of running a restaurant, 
managing a household, or balancing university coursework, finding the time and resources to eat well can be a constant challenge. This is why we created Preppin'—to simplify the process of healthy eating 
and meal planning. By integrating smart technology to track food inventory and offering personalized meal plans with convenient grocery delivery, Preppin' aims to make nutritious eating accessible and manageable, 
no matter how hectic life gets.

**What it does**

Users—including restaurant owners, families, and busy university students—can either manually enter their leftover foods or upload a photo of a grocery receipt. The program then reads and extracts the food items 
listed on the receipt. It processes this data to generate links to recipes sourced from the internet that use the available ingredients.

Additionally, Preppin' offers a subscription-based service that includes a survey to assess users' dietary needs and goals. Based on the survey results, Preppin' creates a customized weekly meal plan and delivers
the fresh groceries required to prepare these meals directly to the user's doorstep.

**How we built it**

For the back-end, we utilized Python, Chat-GPT API to process data, and the tesseract module to read images. Our frontend was made largely with javascript, html, and css, with the backend and frontend connected 
with the flask framework.

**Challenges we ran into**

One of our biggest challenges was integrating our backend system with the frontend display. Our application needed to handle user inputs from the frontend—such as item lists and image uploads—which had to be 
sent to the backend Python program for processing. Once processed, the data needed to be sent back to the frontend website. As first-time users of the Flask framework, we faced difficulties in synchronizing
the frontend and backend components of our project.

**Accomplishments that we're proud of**

Through the countless struggles, our biggest technical accomplishment is creating a functional backend program that integrates with the ChatGPT API to accept user prompts. This achievement not only required 
extensive coding and troubleshooting, but also a long night full of hard work and dedication to ensure smooth interactions between the API and our backend, allowing for real-time processing of user inputs.

Another significant accomplishment is our ability to brainstorm an idea and bring it to life within the short 24-hour timeframe. This involved fast planning as well as execution, showcasing our team's ability 
to work efficiently and collaboratively under pressure. The result is Preppin', a project that we are extremely proud of that has huge potential to better society.

**What we learned**

Throughout this project, we developed our programming knowledge and skills by learning many things along the way. Through many hours, our group learned and refined many backend programming skills, allowing us 
to familiarize ourselves with Python, Flask, and Tesseract. Aside from backend development, our group learned how to better utilize javascript, html, and css, allowing us to build a beautiful website while refining 
our frontend development abilities.

**What's next for Preppin'**

Looking ahead, Preppin' is set to undertake several exciting next steps to further enhance our service. We plan to develop a robust analytics dashboard for users to track their dietary habits, ingredient usage, 
and recipe popularity, providing valuable insights to refine their meal planning. We will also integrate a feature that allows users to set dietary goals and receive customized recommendations based on their nutritional needs. 
To improve accessibility, we aim to launch a mobile app that offers all the functionalities of our web platform on the go. Additionally, we will explore integrating with smart kitchen appliances for seamless recipe execution and real-time 
inventory tracking. By focusing on these advancements, we aim to make Preppin' an indispensable tool for efficient, personalized, and innovative meal management.

**Built With**

- chat-gpt
- css
- flask
- html
- javascript
- python
- tesseract
