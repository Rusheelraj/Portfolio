from flask import Flask, render_template

app = Flask(__name__)

# Sample data for resume
resume_data = {
    "name": "$ whoami - Rusheel Raj Panakadan",
    "title": "Cybersecurity Analyst",
    "email": "rusheelraj.p@gmail.com",
    "location": "Florida, USA",
    "about": "I am currently exploiting the weakness in computer systems and networks, consequently working on Cyber Forensics.",
    "experience": [
        {
            "title": "Research Assistant - Cybersecurity",
            "company": "Florida Tech",
            "location": "Florida, USA",
            "dates": "January 2023 - December 2023",
            "bullet_points": [
                "Implemented a local DNS server with DNSSEC, DOT, and DOH, reducing DNS query response time by 35.2% and enhancing network defense security and performance.",
                "Applied Moving target defense (MTD) strategies on 2 Ubuntu VM’s against DNS flooding attacks in an SDN environment.",
                "Engineered in extracting and analyzing forensic disk images from storage devices, utilizing tools such as dd, Autopsy and FTK.",
                "Conducted malware analysis on three diverse operating systems, facilitating the creation of a comprehensive dataset."
                ]
        },
        {
            "title": "Software Security Test Engineer",
            "company": "Wipro",
            "location": "Hyderabad, India",
            "dates": "June 2019 - June 2022",
            "bullet_points": [
                "Spearheaded bug identification and reporting initiatives for Windows 11 OS, driving a transformative 60% enhancement in system stability and reliability, elevating product quality standards.",
                "Pioneered comprehensive testing protocols for antivirus solutions, executing malware and viruses in controlled environments, resulting in a remarkable 35% improvement in threat detection efficacy and bolstering cybersecurity defenses.",
                "Championed the fortification of Microsoft Defender within the OS, culminating in a substantial 30% increase in malware detection and incident response rates, thereby ensuring strong protection against evolving cyber threats.",
                "Orchestrated thorough evaluation of network and port scanners, including Wireshark, Nessus, and Advanced IP Scanner, optimizing compatibility and functionality to meet stringent performance standards.",
                "Applied advanced analysis techniques to Windows event logs (security, system, application) and crash logs, unveiling software bugs and vulnerabilities, leading to a significant 20% reduction in system risks and enhancing overall system integrity."
            ]
        },
        {
            "title": "Security Engineer Intern",
            "company": "CERT-IN (Indian Computers Emergency Response Team)",
            "location": "Delhi, India",
            "dates": "December 2018 - April 2019",
            "bullet_points": [
                "Executed successful RCE (Remote Code Execution) on Apache2 Struts, Drupal 7, and SMB servers, bolstering penetration testing expertise and fortifying system defenses against critical vulnerabilities.",
                "Enhanced security protocols with Nmap, Nessus, and Metasploit, driving a 40% surge in vulnerability detection and efficiency",
                "Revamped threat detection capabilities through thorough analysis of over 1000 logs with the ELK stack, resulting in a 50% increase in early threat detection and proactive risk mitigation."
            ]
        }
    ],
    "education": [
        {
            "degree": "Master of Science",
            "major": "Information Assurance and Cybersecurity",
            "university": "Florida Tech",
            "location": "Florida, USA",
            "dates": "August 2022 - Present",
            "gpa": "4.0 / 4.0"
        },
        {
            "degree": "Post Graduate Diploma",
            "major": "Cybersecurity",
            "university": "Amity University",
            "location": "Remote / Noida, India",
            "dates": "July 2020 - September 2021",
            "gpa": "9.07 / 10"
        },
        {
            "degree": "Bachelor of Technology",
            "major": "Computer Science",
            "university": "Vel Tech R&D Institute of Science and Technology",
            "location": "Chennai, India",
            "dates": "August 2015 - July 2019",
            "gpa": "8.65 / 10"
        }
    ],
    "skills": {
        "Programming Languages": ["Python", "C", "C++", "Java"],
        "Cybersecurity Tools": ["ELK Stack", "Splunk", "Snort", "Nmap", "Nessus", "Wireshark", "Metasploit", "Burpsuite", "Postman", "Autopsy", "FTK Imager", "Sleuthkit", "Volatility 2 & 3", "Radare2", "Ghidra", "Kali Linux", "Docker", "Virtualbox", "VMWare"],
    },
   "ctf": [
	"National Cyber League - Individual - Rank 99/7404 - Spring 2024",
	"Ranked - 2 in WiCyS CTF - Fall 2023",
	"Ranked - 6 in Amazon-WiCyS CTF - Fall 2023",
	"National Cyber League - Individual - Rank 50/7930 - Fall 2023",
	"National Cyber League - Team Game - Rank 7/316 - Spring 2023"
    ],
    "projects": [
        "Analysis of popular industry-used Wi-Fi hacking tools, Aircrack-ng, Reaver, Wifite and Fern Wi-Fi Cracker",
        "A Biometric Privacy Analysis of Image Cloaking Methods against Face Recognition Algorithm",
        "Hosting a website and analyzing traffic in the TOR network",
        "Applied digital forensics on a fictional case study",
        "Re-creating hashdump plugin in Volatility - 3"
    ],
    "interests": "Apart from being a cyber security analyst, I enjoy most of my time being explored. In the winter, I read e-books and spend most of the time on bed listening music. That would give me a boost :) During the warmer months, I would play Cricket and workout. When forced indoors, I follow a number of love and thriller genre movies and television shows, I loved to watch Sherlock. That is one of my favorites in TV Series. I am an aspiring psychologist. Lol, that seems funny right. But its important for a cyber security personnel to possess social engineering skills. I spend a large amount of my free time exploring the latest technology advancements in the Cyber Security.",
    "certifications": [
        {"name": "NCL Spring 2024 Individual Game - Issued May 2024", "url":"https://cyberskyline.com/report/BN94N1U6TAB1"},
        {"name": "arcX Cyber Threat Intelligence 101", "url":"https://arcx.io/verify-certificate?id=bd4a3df3de52d932eafea9e6db94b9c9d7d39e0e&k=759c8b01fd9a4e0d8f14dd6858ec276a"},
        {"name": "API Penetration Testing - APISEC University", "url":"https://www.credly.com/badges/82757515-d756-4b33-a297-d2fb183cbb5a/linked_in_profile"},
        {"name": "NCL Fall 2023 Individual Game - Issued Nov 2023", "url":"https://cyberskyline.com/report/W4R7JNPBMAQ7"},
        {"name": "NCL Spring 2023 Team Game - Issued May 2023", "url":"https://cyberskyline.com/report/FN2FX4GTJQBE"},
        {"name": "Digital Forensics - Autopsy by Basis Technology", "url":"https://training.sleuthkitlabs.com/certificates/y3eeklb2ca"},
        {"name":"Completion of Ethical Hacking, Basic & Advanced Penetration Testing - Cybrary"}
    ]
}

@app.route('/')
def index():
    return render_template('index.html', resume=resume_data)

if __name__ == '__main__':
    app.run(debug=True)
