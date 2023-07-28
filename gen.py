import openai
import os

def ask_GPT4(prompt): 
    result = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=[{"role": "system", "content": "n/a"},
                                                    {"role": "user", "content": prompt}])
    return result['choices'][0]['message']['content']

# Load OpenAI API key from file
with open("openai_api_key.txt", "r", encoding="utf-8") as f:
    openai.api_key = f.read().strip()

# Load company names from file
with open("company_names.txt", "r", encoding="utf-8") as f:
    company_names = [line.strip() for line in f]

# Generate personalized emails for each company
for company_name in company_names:
    # Construct email message
    message = f"You are an email-writing bot that writes personalized emails on behalf of the CEO of DNAnalyzer, an open source project that is also a fiscally sponsored nonprofit by Hack Club made by high school students that aims to revolutionize the field of DNA analysis by using innovative AI-powered analysis and interpretive tools1.  It can reveal the hidden patterns and properties of DNA sequences, such as gene expression, methylation, transcription factors, and more2. It also provides a variety of other useful tools, such as a built-in DNA sequence editor, viewer, generator, and converter. For your context, DNAnalyzer is a relatively new and smaller (100 stars on GitHub) open source project on GitHub. You are to write a 4 paragraph email to (company name and brief description of it: {company_name}) describing DNAnalyzer and asking for their help in any way (you get to determine what form of help this specific organization can help DNAnalyzer with). We would greatly appreciate a partnership for DNAnalyzer. If not, we would also appreciate guidance and/or resources to develop whatever that company made for our nonprofit. Here is an example email that I wrote for Google Alphafold (DO NOT USE THIS AS A TEMPLATE, rather take loose inspiration from it): nHello Members of the AlphaFold Project" + "We are high school students who have a keen interest in biology and the interesting field of proteomics and nucleic acids. We are writing to show our enthusiasm for Alphafold's ground-breaking work and would like to ask for tips and possible methods of thinking/logic that came into developing Alpha Fold, which we could apply to our non-profit called DNAnalyzer. DNAnalyzer is a newly started project where we hope to combine open-source technology and create novel algorithms that can help detect different disorders and link al" + "We have taken great interest in the ground-breaking work of protein folding by Alpha Fold, which holds great promise for reshaping our understanding of cellular functions. We are impressed by how Alphafold has used machine learning to predict tertiary structures of proteins to a high level accuracy, opening the door for significant developments across a range of medicinal and therapeutic applications. We believe that " + "We are curious to find out more about the ideas and processes used to develop technology at Alphafold. It's exciting to learn how you used machine learning techniques to examine and forecast protein folding. We would be very grateful for any information on the fundamental ideas and strategies that were essential to the development of an AI or ML model, as we hope to use neural networks and other critical tools to help develop our platform. Our organization has a strong interest in investigating how artificial intelligence and machine learning might be used to examine DNA sequences and the central dogma. " + "In the area of DNA and protein sequence analysis, we were wondering if you could offer some advice or resources on how high school students may get started with machine learning. Are there any tools, suggestions, datasets that we can access in genomics to start this work (we know of PDBs for example, but not of many other sources). Are there any research papers, or literature that would be of use in bioinformatics?"
    
    # Generate email using OpenAI API
    response = ask_GPT4(message)

    # Save email to file
    email_filename = f"emails/{company_name[:10]}.txt"
    os.makedirs(os.path.dirname(email_filename), exist_ok=True)
    with open(email_filename, "w") as f:
        f.write(response.strip())
