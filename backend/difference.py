class Differences:
    def __init__(self):
        self.current_skills = []
        self.required_skills = []
        self.percentage_of_skills_known = null
        self.all_Skills = ["Python", "JavaScript", "Java", "C++", "C#", "Ruby", "Go", "Swift", "PHP", "Django"
                       , "Flask", "Ruby on Rails", "Ruby", "Angular", "React", "Vue.js", "ASP.NET", "SQL", "NoSQL", "MongoDB",
                       "MySQL", "PostgreSQL", "OracleDB", "Firebase", "Docker", "Kubernetes", "Jenkins", "Git", "Terraform",
                       "Ansible", "CI/CD Pipelines", "AWS", "Google Cloud Platform", "Amazon Web Services", "Microsoft Azure", "Azure",
                       "IBM Cloud", "Git", "GitHub", "GitLab", "Bitbucket", "Restful APIs", "GraphQL", "gRPC", "TensorFlow", "PyTorch",
                       "Pandas", "NumPy", "Scikit-Learn", "R", "Testing Tools", "Selenium", "JUnit", "Postman", "Mocha", "Chai",
                       "JIRA", "Trello", "Asana", "Monday.com", "Microsoft Project", "Project Management Methodologies", "Agile", 
                       "Scrum", "Kanban", "Waterfall", "Linux", "Windows", "macOS", "TCP", "IP", "VPN", "Firewalls", "SSL/TLS",
                       "Adobe XD", "Figma", "Sketch", "InVision", "Docker", "Kubernetes", "Agile Methodologies" ]

    def get_difference_in_skills(result, job_description):
    #shout print out 
        for skill in result.skills:
            self.current_skills.append(skill)


        for skill in all_Skills:
            if skill in job_description:
                self.required_skills.append(skill)

        
        self.percentage_of_skills_known = (current_skills/required_skills) * 100



            



