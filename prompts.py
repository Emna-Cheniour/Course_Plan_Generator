generate_educational_content="""
You are a teacher and you will be preparing educational courses
 Generate an educational course plan based on the following  content  :
 %START OF CONTENT
\n{content}\n
%END OF CONTENT
Ensure that the course plan is structured logically and pedagogically,
favoring a natural progression of understanding. 
Please provide a detailed plan, highlighting
the main sections, subsections, and planned activities. 

Format of the output : 
    Introduction: 3-4 lines to present the course topic and learning objectives \n
    Course Content: a 10 lines paragraph in which you talk in Details of the main concepts, theories, and information to be covered,\n
    and include Concrete Examples To illustrate key concepts,\n
    Practical Exercises and Activities: To reinforce understanding,\n
    Conclusion: RAW text 2-3 lines to summarize the key points of the course and encourage the learner to continue their studies.\n
%END OF THE FORMAT OF THE OUTPUT

I will give a example so that you could understand more:\n
but it's just an example so you're not supposed to copy  content from it,it's based on specific input cotent ,
Dont'copy the content of the Example1 ,it's just an example
% START OF EXAMPLE1

%START OF OUTPUT you are supposed to generate  in  EXAMPLE1

  Introduction: In this course, we'll delve into the transformative world of Artificial Intelligence (AI), exploring its fundamental concepts and applications. We'll begin by understanding the basic principles and significance of AI, setting clear learning objectives for our journey,
  AI Fundamentals: We'll start with the fundamentals of AI, covering machine learning, neural networks, and data analysis, providing a solid foundation for our exploration.,
  Benefits of AI: This section will focus on the myriad benefits of AI, such as enhancing efficiency, boosting productivity, and driving innovation across industries. We'll discuss real-world use cases, like healthcare, finance, and transportation, where AI has made a substantial impact.,
  Revolutionizing Healthcare: We'll dive deeper into AI's impact on healthcare, discussing how it aids in disease diagnosis, treatment recommendations, and predictive analytics. This has led to better patient care and cost reduction.,
  AI in Transportation: Here, we'll explore the exciting world of autonomous vehicles and their potential to reshape the way we travel. We'll also discuss how AI minimizes accidents and enhances safety on our roads.,
  Transforming Education: "Education is not left untouched by AI. In this section, we'll look at AI-driven personalized learning platforms and their ability to improve education quality. Additionally, we'll discuss how AI supports educators in administrative tasks, giving them more time to teach effectively.,
  AI in Business: AI's role in business is significant. We'll examine how AI empowers data-driven decision-making and streamlines operations. Automation reduces the workload and allows employees to focus on strategic activities.,
  AI in Creative Industries: AI's creative potential is astounding. We'll discuss how AI generates music, art, and assists in film production, offering new avenues for artists and creatives to explore.,
  Innovation and Research: Lastly, we'll explore how AI accelerates innovation in research and development. From drug discovery to materials science, AI speeds up complex processes, enabling groundbreaking discoveries.,
  ,
  Practical Application: 
    Case Studies: To illustrate AI's benefits, we'll analyze real-world case studies in various domains, reinforcing our understanding of AI's impact.,
    Hands-On Exercises: We'll engage in hands-on exercises, allowing students to apply AI concepts practically and gain valuable skills.,
  ,
  Conclusion: In conclusion, we'll summarize the key benefits of AI and its profound impact on society. We'll encourage learners to continue their AI journey, highlighting its importance in the digital age and the numerous opportunities it presents.,
%END OF OUTPUT you are supposed to generate  in  EXAMPLE1
Dont'copy the content of the Example1 ,it is  just an example based on a artificial inteligence article 
"""

is_relevant_template = """
You are a course evaluator. Your task is to determine whether the following text has the potential for educational content:
{extracted_text}
Do not be strict \n
Please be lenient in your evaluation and consider various factors, such as the depth of information, clarity, and relevance to an educational context. Respond with 'True' if the text has potential for educational content, and 'False' if it does not.\n

Format of Output:
The output should be a boolean value. Return 'True' if the content is relevant for education, and 'False' if it is not.
"""


translate_template= """You will be provided with the sample text \n
    Your task is to translate the text into {output_language} language \n
    please pay attention to the context and keep in mind that what you are supposed to do is to keep the same meaning but in the  {output_language} .\n
    so do not just translate the text literally just focus on keeping the same meaning .\n
    """

