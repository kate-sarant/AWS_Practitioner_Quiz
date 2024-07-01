class Question:
    def __init__(self, prompt, options, correct_option):
        self.prompt = prompt
        self.options = options
        self.correct_option = correct_option
        
questions = [
    Question("What is the function of an AWS region?", 
             ["A. To provide access control to AWS resources",
              "B. To isolate resources within the same account",
              "C. To maintain geographic presence of AWS infrastructure",
              "D. None of the above"], "C"),
              
    Question("What AWS service allows you to analyze and visualize data in real-time using dashboards and visualizations?", 
             ["A. Amazon QuickSight",
              "B. Amazon Kinesis",
              "C. Amazon Neptune",
              "D. Amazon Elasticsearch"], "A"),
 
    Question("Which AWS service provides scalable cloud storage?", 
             ["A. Amazon Glacier",
              "B. Amazon DynamoDB",
              "C. Amazon S3",
              "D. Amazon RDS"], "C"),

    Question("What is the primary purpose of Amazon EC2?", 
             ["A. Managed File Storage",
              "B. Scalable Load Balancing",
              "C. Virtual Servers in the Cloud",
              "D. Data Warehousing"], "C"),
              
     Question("What is the primary purpose of Amazon EC2?", 
             ["A. Managed File Storage",
              "B. Scalable Load Balancing",
              "C. Virtual Servers in the Cloud",
              "D. Data Warehousing"], "C"),

    Question("Which AWS service is used for real-time data processing?", 
             ["A. Amazon Redshift",
              "B. Amazon RDS",
              "C. Amazon Kinesis",
              "D. Amazon EC2"], "C"),

    Question("What is the storage service provided by AWS that is designed for high durability and availability?", 
             ["A. Amazon S3",
              "B. Amazon EBS",
              "C. Amazon Glacier",
              "D. Amazon Aurora"], "A"),

    Question("What AWS service allows you to deploy and manage containerized applications?", 
             ["A. Amazon EC2",
              "B. Amazon Lambda",
              "C. Amazon ECS",
              "D. Amazon S3"], "C"),

    Question("Which AWS service is a fully managed message queuing service?", 
             ["A. Amazon SQS",
              "B. Amazon SNS",
              "C. Amazon Glacier",
              "D. Amazon Athena"], "A"),
              
    Question("What AWS service enables developers to build, train, and deploy machine learning models?", 
             ["A. Amazon SageMaker",
              "B. Amazon Lex",
              "C. Amazon Polly",
              "D. Amazon Rekognition"], "A"),
    Question("What is an IAM Policy?", 
             ["A. A document that customizes user permissions for AWS services and resources",
              "B. A tool for managing virtual servers in the cloud",
              "C. A service for real-time data processing",
              "D. A database service for high durability and availability"], "A"),

    Question("Which IAM entity can be used for assigning permissions to AWS services?", 
             ["A. IAM Policy",
              "B. IAM Role",
              "C. IAM Group",
              "D. IAM User"], "A"),

    Question("Which perspective of the AWS Cloud Adoption Framework focuses on minimizing the business risks?", 
             ["A. Governance Perspective",
              "B. Security Perspective",
              "C. Operations Perspective",
              "D. People Perspective"], "A"),

    Question("Which AWS service helps you build text chatbots?", 
             ["A. Amazon Lex",
              "B. Amazon Polly",
              "C. Amazon Rekognition",
              "D. Amazon Sumerian"], "A"),

    Question("If an instance store reboots, does the data in the instance persist?", 
             ["A. Yes",
              "B. No"], "B"),

    Question("Which sentence best describes AWS CloudWatch?", 
             ["A. CloudWatch is a monitoring service that monitors your resources, and configures automatic alarms.",
              "B. CloudWatch is a database service for high availability and scalability.",
              "C. CloudWatch is a content delivery network service.",
              "D. CloudWatch is a blockchain platform."], "A"),

   Question("Based on application's network requests, AWS Web Application Firewall can block network traffic.", 
             ["A. True",
              "B. False"], "A"),

  Question("Which AWS service manages encryption and decryption of data?", 
             ["A. AWS Key Management Service (AWS KMS)",
              "B. Amazon Redshift",
              "C. Amazon RDS",
              "D. Amazon S3"], "A"),

    Question("How is called a service that lets you run code without needing to think about servers?", 
             ["A. AWS Lambda",
              "B. Amazon EC2",
              "C. Amazon S3",
              "D. Amazon RDS"], "A"),
 
    Question("Which AWS database service provides historical data of your application changes?", 
             ["A. Amazon RDS",
              "B. Amazon Redshift",
              "C. AWS Quantum Ledger Database",
              "D. Amazon DynamoDB"], "C"), 
              
    Question("Which of the below are components that can be configured in the VPC section of the AWS management console?", 
             ["A. EBS volumes",
              "B. dns records",
              "C. subnet and endpoints",
              "D.elastic load balancer"], "C"),

    Question("What does AWS IAM stand for?", 
             ["A. Amazon Web Services Integration and Management",
              "B. Amazon Identity and Access Management",
              "C. Amazon Web Server Instances Management",
              "D. Amazon Infrastructure and Application Monitoring"], "B"),

   Question("A Cloud Practitioner noticed that IP addresses that are owned by AWS are being used to attempt to\nflood ports on some of the company’s systems.\nTo whom should the issue be reported?", 
             ["A. professional services ",
              "B. aws trust and safety team",
              "C. TAM",
              "D. APN"], "B"),
    
    Question("What is the best practice for managing AWS IAM access keys?", 
             ["A. there is no need to manage access keys ",
              "B. never use access keys, always use iam roles",
              "C. aws rotate access keys on a schedule",
              "D. customers should rotate access keys regularly"], "D"),
    Question("Which AWS service is used for scalable object storage in the cloud?", 
             ["A. Amazon EC2",
              "B. Amazon S3",
              "C. Amazon RDS",
              "D. Amazon ElastiCache"], "B"),

    Question("Which AWS service allows you to provision cloud resources using text files?", 
             ["A. AWS CloudFormation",
              "B. AWS Lambda",
              "C. Amazon SQS",
              "D. Amazon Kinesis"], "A"),

    Question("What type of database service is Amazon RDS known for?", 
             ["A. NoSQL database",
              "B. In-memory database",
              "C. Relational database",
              "D. Time-series database"], "C"),

    Question("Which AWS service allows you to securely control access to AWS resources?", 
             ["A. Amazon Lex",
              "B. AWS WAF",
              "C. AWS Shield",
              "D. AWS IAM"], "D"),

    Question("In AWS, what is the term used for the process of copying data from one storage system to another?", 
             ["A. Data migration",
              "B. Data replication",
              "C. Data synchronization",
              "D. Data transformation"], "A"),

    Question("What AWS service enables you to monitor and troubleshoot your networks?", 
             ["A. AWS CloudTrail",
              "B. Amazon CloudFront",
              "C. Amazon VPC",
              "D. AWS Direct Connect"], "C"),

    Question("Which AWS service offers a managed blockchain platform?", 
             ["A. Amazon ECS",
              "B. Amazon EKS",
              "C. Amazon Managed Blockchain",
              "D. Amazon RDS"], "C"),

    Question("Which AWS service provides scalable computing capacity?", 
             ["A. Amazon S3",
              "B. Amazon EC2",
              "C. Amazon SQS",
              "D. AWS Lambda"], "B"),

    Question("What does the Amazon S3 service offer in terms of data storage?", 
             ["A. File storage",
              "B. Block storage",
              "C. Object storage",
              "D. Database storage"], "C"),

    Question("Which AWS service enables you to build, train, and deploy machine learning models?", 
             ["A. Amazon SageMaker",
              "B. Amazon Polly",
              "C. Amazon Rekognition",
              "D. Amazon Translate"], "A"),

    Question("What is the AWS service that provides a simple way to find, test, buy, and deploy third-party software?", 
             ["A. AWS Cloud Marketplace",
              "B. AWS Management Console",
              "C. AWS Config",
              "D. AWS Organizations"], "A"),

    Question("What AWS service enables you to send and receive messages between software components?", 
             ["A. Amazon SQS",
              "B. AWS Direct Connect",
              "C. Amazon Neptune",
              "D. Amazon Route 53"], "A"),

    Question("In AWS, what does VPC stand for?", 
             ["A. Virtual Personal Connection",
              "B. Virtual Public Cloud",
              "C. Virtual Private Cloud",
              "D. Virtual Protocol Controller"], "C"),

    Question("Which AWS service provides a fully managed service for running Microsoft Windows applications?", 
             ["A. Amazon EKS",
              "B. Amazon ECS",
              "C. AWS Directory Service",
              "D. Amazon RDS for SQL Server"], "D"),

    Question("What is the primary benefit of using AWS Elastic Beanstalk?", 
             ["A. Automated database backups",
              "B. Automated resource scaling",
              "C. Automated software updates",
              "D. Automated security patches"], "B"),

    Question("Which AWS service provides a data warehouse solution?", 
             ["A. Amazon Aurora",
              "B. Amazon Redshift",
              "C. Amazon Neptune",
              "D. Amazon DynamoDB"], "B"),

    Question("What AWS service allows you to monitor and analyze log data from your AWS infrastructure?", 
             ["A. AWS X-Ray",
              "B. AWS CloudWatch Logs",
              "C. AWS Config",
              "D. AWS Inspector"], "B"),

    Question("Which AWS service provides a distributed, fault-tolerant, and scalable database system?", 
             ["A. Amazon RDS",
              "B. Amazon DynamoDB",
              "C. Amazon Redshift",
              "D. Amazon ElastiCache"], "B"),

    Question("What does the term 'resilient' mean in relation to AWS services?", 
             ["A. High availability and fault tolerance",
              "B. Low cost and high performance",
              "C. Scalability and elasticity",
              "D. Compliance and security"], "A"),

    Question("Which AWS service provides a code hosting source control service?", 
             ["A. AWS CodePipeline",
              "B. AWS CodeBuild",
              "C. AWS CodeCommit",
              "D. AWS CodeDeploy"], "C"),

    Question("What AWS service allows you to create and manage virtual private networks?", 
             ["A. Amazon VPC",
              "B. AWS VPN",
              "C. AWS Direct Connect",
              "D. AWS Transit Gateway"], "A"),

    Question("Which AWS service provides a content delivery network to distribute content globally?", 
             ["A. Amazon S3",
              "B. AWS Direct Connect",
              "C. Amazon CloudFront",
              "D. Amazon Route 53"], "C"),

    Question("What AWS service enables you to automate the deployment of applications?", 
             ["A. AWS CodePipeline",
              "B. AWS CodeDeploy",
              "C. AWS CodeCommit",
              "D. AWS CodeBuild"], "B"),
#65
    Question("In AWS, what is the term used for automatic scaling of cloud resources based on traffic or performance metrics?", 
             ["A. Elastic Load Balancing",
              "B. Auto Scaling",
              "C. Bursting",
              "D. Pooled Capacity"], "B"),        
   
]

def run_quiz(questions):
    score = 0
    counter = 0
    wrong_answer = []
    correct_choice=0
    for question in questions:
        counter+=1
        print('\n Question',counter,": ", question.prompt,'\n')
        for index,option in enumerate(question.options):
            print(question.options[index])
            #store the index of the correct answer
            correct_choice=index
        answer = input("Enter your choice (A, B, C, or D): ").upper()
        if  answer == question.correct_option:
            score += 1
            print("Correct!")
        else:             
            print("Correct answer: ",question.correct_option)
            #append the question and the answer of faulty question.
            wrong_answer.append('Q:'+str(counter)+' '+question.prompt+" A:"+question.options[correct_choice])  

    #print the end score
    print(f"You got {score}/{len(questions)} questions correct.")
    #print the wrong answers
    print('Wrong answers are: ', *wrong_answer, sep='\n\n')
    if score >= len(questions)-10 :
        print("Congratulations! You passed the AWS Cloud Practitioner Certification Quiz.")
    else:
        print("Unfortunately, you did not pass the AWS Cloud Practitioner Certification Quiz.")


run_quiz(questions)
