class Differences:
    def __init__(self):
        self.current_skills = []
        self.required_skills = []
        self.missing_skills = []
        self.percentage_of_skills_known = 0
        self.all_Skills = ["Python", "JavaScript", "Java", "C++", "C#", "Ruby", "Go", "Swift", "PHP", "Django"
                       , "Flask", "Ruby on Rails", "Ruby", "Angular", "React", "Vue.js", "ASP.NET", "SQL", "NoSQL", "MongoDB",
                       "MySQL", "PostgreSQL", "OracleDB", "Firebase", "Docker", "Kubernetes", "Jenkins", "Git", "Terraform",
                       "Ansible", "CI/CD Pipelines", "AWS", "Google Cloud Platform", "Amazon Web Services", "Microsoft Azure", "Azure",
                       "IBM Cloud", "Git", "GitHub", "GitLab", "Bitbucket", "Restful APIs", "GraphQL", "gRPC", "TensorFlow", "PyTorch",
                       "Pandas", "NumPy", "Scikit-Learn", "R", "Testing Tools", "Selenium", "JUnit", "Postman", "Mocha", "Chai",
                       "JIRA", "Trello", "Asana", "Monday.com", "Microsoft Project", "Project Management Methodologies", "Agile", 
                       "Scrum", "Kanban", "Waterfall", "Linux", "Windows", "macOS", "TCP", "IP", "VPN", "Firewalls", "SSL/TLS",
                       "Adobe XD", "Figma", "Sketch", "InVision", "Docker", "Kubernetes", "Agile Methodologies" ]

    def get_difference_in_skills(self, result, job_description):
        self.current_skills = result.get('skills', [])
        self.required_skills = [skill for skill in self.all_skills if skill in job_description]
        if self.required_skills:
            self.percentage_of_skills_known = (len(self.current_skills) / len(self.required_skills)) * 100
        else:
            self.percentage_of_skills_known = 0
        
        for skill in result.skills:
            self.current_skills.append(skill)
        
        self.missing_skills = [skill for skill in self.required_skills if skill not in self.current_skills]


        return {
            "percentage_known": self.percentage_of_skills_known,
            "missing_skills": self.missing_skills
    
        }



            




            



