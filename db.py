from pymongo import MongoClient
import json

# Task data to be inserted
tasks_data = [
    
    {
        "task_name": "Refactor Legacy Code",
        "complexity": "High",
        "size": "Large",
        "task_type": "Development",
        "description": "Improve the existing codebase to enhance maintainability and performance.",
        "estimated_effort_hours": 70,
        "confidence_level": "Medium",
        "estimated_range_hours": "65-75"
    },
    {
        "task_name": "Write API Documentation",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Development",
        "description": "Create comprehensive documentation for the existing APIs.",
        "estimated_effort_hours": 15,
        "confidence_level": "Low",
        "estimated_range_hours": "12-18"
    },
    {
        "task_name": "Test Performance of Application",
        "complexity": "High",
        "size": "Large",
        "task_type": "Testing",
        "description": "Conduct performance testing to ensure application meets performance standards.",
        "estimated_effort_hours": 55,
        "confidence_level": "High",
        "estimated_range_hours": "50-60"
    },
    {
        "task_name": "Develop New Feature X",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Development",
        "description": "Implement new feature X as described in the requirements document.",
        "estimated_effort_hours": 40,
        "confidence_level": "Medium",
        "estimated_range_hours": "35-45"
    },
    {
        "task_name": "Fix Critical Bug in Module Y",
        "complexity": "High",
        "size": "Small",
        "task_type": "Development",
        "description": "Identify and resolve the critical bug in Module Y.",
        "estimated_effort_hours": 20,
        "confidence_level": "High",
        "estimated_range_hours": "18-22"
    },
    {
        "task_name": "Optimize Database Queries",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Development",
        "description": "Optimize database queries to improve application performance.",
        "estimated_effort_hours": 35,
        "confidence_level": "Medium",
        "estimated_range_hours": "30-40"
    },
    {
        "task_name": "Design UI Mockups",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Create UI mockups for the new application interface.",
        "estimated_effort_hours": 10,
        "confidence_level": "High",
        "estimated_range_hours": "8-12"
    },
    {
        "task_name": "Implement Security Features",
        "complexity": "High",
        "size": "Large",
        "task_type": "Development",
        "description": "Add new security features to enhance application security.",
        "estimated_effort_hours": 60,
        "confidence_level": "Medium",
        "estimated_range_hours": "55-65"
    },
    {
        "task_name": "Conduct User Research",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Development",
        "description": "Conduct user research to gather insights for product improvement.",
        "estimated_effort_hours": 25,
        "confidence_level": "Medium",
        "estimated_range_hours": "20-30"
    },
    {
        "task_name": "Setup CI/CD Pipeline",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Development",
        "description": "Set up a continuous integration and continuous delivery pipeline.",
        "estimated_effort_hours": 30,
        "confidence_level": "Medium",
        "estimated_range_hours": "25-35"
    },
    {
        "task_name": "Write Unit Tests",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Testing",
        "description": "Write unit tests for the existing codebase to ensure code quality.",
        "estimated_effort_hours": 15,
        "confidence_level": "High",
        "estimated_range_hours": "12-18"
    },
    {
        "task_name": "Upgrade Server Infrastructure",
        "complexity": "High",
        "size": "Large",
        "task_type": "Infrastructure",
        "description": "Upgrade the existing server infrastructure to support higher traffic.",
        "estimated_effort_hours": 80,
        "confidence_level": "Medium",
        "estimated_range_hours": "75-85"
    },
    {
        "task_name": "Create Marketing Campaign",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Marketing",
        "description": "Develop a marketing campaign to promote the new product release.",
        "estimated_effort_hours": 50,
        "confidence_level": "Medium",
        "estimated_range_hours": "45-55"
    },
    {
        "task_name": "Implement OAuth Authentication",
        "complexity": "High",
        "size": "Medium",
        "task_type": "Development",
        "description": "Integrate OAuth authentication for secure user login.",
        "estimated_effort_hours": 45,
        "confidence_level": "Medium",
        "estimated_range_hours": "40-50"
    },
    {
        "task_name": "Develop Mobile App",
        "complexity": "High",
        "size": "Large",
        "task_type": "Development",
        "description": "Develop a mobile application version of the existing web app.",
        "estimated_effort_hours": 100,
        "confidence_level": "Medium",
        "estimated_range_hours": "90-110"
    },
    {
        "task_name": "Perform Code Review",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Development",
        "description": "Perform a thorough code review to ensure adherence to coding standards.",
        "estimated_effort_hours": 8,
        "confidence_level": "High",
        "estimated_range_hours": "6-10"
    },
    {
        "task_name": "Setup Monitoring Tools",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Infrastructure",
        "description": "Set up monitoring tools to track application performance and uptime.",
        "estimated_effort_hours": 35,
        "confidence_level": "Medium",
        "estimated_range_hours": "30-40"
    },
    {
        "task_name": "Optimize Frontend Performance",
        "complexity": "High",
        "size": "Medium",
        "task_type": "Development",
        "description": "Optimize frontend performance to improve page load times and user experience.",
        "estimated_effort_hours": 45,
        "confidence_level": "Medium",
        "estimated_range_hours": "40-50"
    },
    {
        "task_name": "Conduct Security Audit",
        "complexity": "High",
        "size": "Large",
        "task_type": "Testing",
        "description": "Conduct a security audit to identify and mitigate potential vulnerabilities.",
        "estimated_effort_hours": 70,
        "confidence_level": "Medium",
        "estimated_range_hours": "65-75"
    },
    {
        "task_name": "Create Data Backup Strategy",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Infrastructure",
        "description": "Develop and implement a data backup strategy to ensure data integrity and availability.",
        "estimated_effort_hours": 25,
        "confidence_level": "High",
        "estimated_range_hours": "20-30"
    },
    
    {
        "task_name": "Refactor Legacy Code",
        "complexity": "High",
        "size": "Large",
        "task_type": "Development",
        "description": "Improve the existing codebase to enhance maintainability and performance.",
        "estimated_effort_hours": 70,
        "confidence_level": "Medium",
        "estimated_range_hours": "65-75"
    },
    {
        "task_name": "Write API Documentation",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Development",
        "description": "Create comprehensive documentation for the existing APIs.",
        "estimated_effort_hours": 15,
        "confidence_level": "Low",
        "estimated_range_hours": "12-18"
    },
    {
        "task_name": "Test Performance of Application",
        "complexity": "High",
        "size": "Large",
        "task_type": "Testing",
        "description": "Conduct performance testing to ensure application meets performance standards.",
        "estimated_effort_hours": 55,
        "confidence_level": "High",
        "estimated_range_hours": "50-60"
    },
    {
        "task_name": "Develop New Feature X",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Development",
        "description": "Implement new feature X as described in the requirements document.",
        "estimated_effort_hours": 40,
        "confidence_level": "Medium",
        "estimated_range_hours": "35-45"
    },
    {
        "task_name": "Fix Critical Bug in Module Y",
        "complexity": "High",
        "size": "Small",
        "task_type": "Development",
        "description": "Identify and resolve the critical bug in Module Y.",
        "estimated_effort_hours": 20,
        "confidence_level": "High",
        "estimated_range_hours": "18-22"
    },
    {
        "task_name": "Optimize Database Queries",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Development",
        "description": "Optimize database queries to improve application performance.",
        "estimated_effort_hours": 35,
        "confidence_level": "Medium",
        "estimated_range_hours": "30-40"
    },
    {
        "task_name": "Design UI Mockups",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Create UI mockups for the new application interface.",
        "estimated_effort_hours": 10,
        "confidence_level": "High",
        "estimated_range_hours": "8-12"
    },
    {
        "task_name": "Implement Security Features",
        "complexity": "High",
        "size": "Large",
        "task_type": "Development",
        "description": "Add new security features to enhance application security.",
        "estimated_effort_hours": 60,
        "confidence_level": "Medium",
        "estimated_range_hours": "55-65"
    },
    {
        "task_name": "Conduct User Research",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Development",
        "description": "Conduct user research to gather insights for product improvement.",
        "estimated_effort_hours": 25,
        "confidence_level": "Medium",
        "estimated_range_hours": "20-30"
    },
    {
        "task_name": "Setup CI/CD Pipeline",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Development",
        "description": "Set up a continuous integration and continuous delivery pipeline.",
        "estimated_effort_hours": 30,
        "confidence_level": "Medium",
        "estimated_range_hours": "25-35"
    },
    {
        "task_name": "Write Unit Tests",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Testing",
        "description": "Write unit tests for the existing codebase to ensure code quality.",
        "estimated_effort_hours": 15,
        "confidence_level": "High",
        "estimated_range_hours": "12-18"
    },
    {
        "task_name": "Upgrade Server Infrastructure",
        "complexity": "High",
        "size": "Large",
        "task_type": "Infrastructure",
        "description": "Upgrade the existing server infrastructure to support higher traffic.",
        "estimated_effort_hours": 80,
        "confidence_level": "Medium",
        "estimated_range_hours": "75-85"
    },
    {
        "task_name": "Create Marketing Campaign",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Marketing",
        "description": "Develop a marketing campaign to promote the new product release.",
        "estimated_effort_hours": 50,
        "confidence_level": "Medium",
        "estimated_range_hours": "45-55"
    },
    {
        "task_name": "Implement OAuth Authentication",
        "complexity": "High",
        "size": "Medium",
        "task_type": "Development",
        "description": "Integrate OAuth authentication for secure user login.",
        "estimated_effort_hours": 45,
        "confidence_level": "Medium",
        "estimated_range_hours": "40-50"
    },
    {
        "task_name": "Develop Mobile App",
        "complexity": "High",
        "size": "Large",
        "task_type": "Development",
        "description": "Develop a mobile application version of the existing web app.",
        "estimated_effort_hours": 100,
        "confidence_level": "Medium",
        "estimated_range_hours": "90-110"
    },
    {
        "task_name": "Perform Code Review",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Development",
        "description": "Perform a thorough code review to ensure adherence to coding standards.",
        "estimated_effort_hours": 8,
        "confidence_level": "High",
        "estimated_range_hours": "6-10"
    },
    {
        "task_name": "Setup Monitoring Tools",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Infrastructure",
        "description": "Set up monitoring tools to track application performance and uptime.",
        "estimated_effort_hours": 35,
        "confidence_level": "Medium",
        "estimated_range_hours": "30-40"
    },
    {
        "task_name": "Optimize Frontend Performance",
        "complexity": "High",
        "size": "Medium",
        "task_type": "Development",
        "description": "Optimize frontend performance to improve page load times and user experience.",
        "estimated_effort_hours": 45,
        "confidence_level": "Medium",
        "estimated_range_hours": "40-50"
    },
    {
        "task_name": "Conduct Security Audit",
        "complexity": "High",
        "size": "Large",
        "task_type": "Testing",
        "description": "Conduct a security audit to identify and mitigate potential vulnerabilities.",
        "estimated_effort_hours": 70,
        "confidence_level": "Medium",
        "estimated_range_hours": "65-75"
    },
    {
        "task_name": "Create Data Backup Strategy",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Infrastructure",
        "description": "Develop and implement a data backup strategy to ensure data integrity and availability.",
        "estimated_effort_hours": 25,
        "confidence_level": "High",
        "estimated_range_hours": "20-30"
    },
    {
        "task_name": "Improve SEO",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Marketing",
        "description": "Enhance website SEO to improve search engine rankings.",
        "estimated_effort_hours": 15,
        "confidence_level": "Medium",
        "estimated_range_hours": "10-20"
    },
    {
        "task_name": "Develop Custom CMS",
        "complexity": "High",
        "size": "Large",
        "task_type": "Development",
        "description": "Create a custom content management system tailored to client needs.",
        "estimated_effort_hours": 120,
        "confidence_level": "Medium",
        "estimated_range_hours": "110-130"
    },
    {
        "task_name": "Conduct A/B Testing",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Testing",
        "description": "Run A/B tests to optimize user experience and conversion rates.",
        "estimated_effort_hours": 30,
        "confidence_level": "Medium",
        "estimated_range_hours": "25-35"
    },
    {
        "task_name": "Create Wireframes",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Design wireframes for the new application layout.",
        "estimated_effort_hours": 10,
        "confidence_level": "High",
        "estimated_range_hours": "8-12"
    },
    {
        "task_name": "Configure Load Balancer",
        "complexity": "High",
        "size": "Large",
        "task_type": "Infrastructure",
        "description": "Set up a load balancer to distribute traffic efficiently.",
        "estimated_effort_hours": 50,
        "confidence_level": "Medium",
        "estimated_range_hours": "45-55"
    },
    {
        "task_name": "Migrate Database",
        "complexity": "High",
        "size": "Large",
        "task_type": "Infrastructure",
        "description": "Migrate the existing database to a new platform.",
        "estimated_effort_hours": 70,
        "confidence_level": "Medium",
        "estimated_range_hours": "65-75"
    },
    {
        "task_name": "Develop Chatbot",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Development",
        "description": "Create a chatbot for customer service automation.",
        "estimated_effort_hours": 40,
        "confidence_level": "Medium",
        "estimated_range_hours": "35-45"
    },
    {
        "task_name": "Create Style Guide",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Develop a comprehensive style guide for consistent branding.",
        "estimated_effort_hours": 15,
        "confidence_level": "High",
        "estimated_range_hours": "10-20"
    },
    {
        "task_name": "Run Penetration Testing",
        "complexity": "High",
        "size": "Large",
        "task_type": "Testing",
        "description": "Conduct penetration testing to identify security vulnerabilities.",
        "estimated_effort_hours": 60,
        "confidence_level": "Medium",
        "estimated_range_hours": "55-65"
    },
    {
        "task_name": "Create Social Media Strategy",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Marketing",
        "description": "Develop a strategy for social media engagement and growth.",
        "estimated_effort_hours": 30,
        "confidence_level": "Medium",
        "estimated_range_hours": "25-35"
    },
    {
        "task_name": "Develop RESTful API",
        "complexity": "High",
        "size": "Large",
        "task_type": "Development",
        "description": "Build a RESTful API for the new application.",
        "estimated_effort_hours": 90,
        "confidence_level": "Medium",
        "estimated_range_hours": "85-95"
    },
    {
        "task_name": "Conduct User Testing",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Testing",
        "description": "Perform user testing to gather feedback and improve usability.",
        "estimated_effort_hours": 25,
        "confidence_level": "Medium",
        "estimated_range_hours": "20-30"
    },
    {
        "task_name": "Create Logo Design",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Design a new logo for the product rebranding.",
        "estimated_effort_hours": 8,
        "confidence_level": "High",
        "estimated_range_hours": "6-10"
    },
    {
        "task_name": "Setup Analytics Dashboard",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Development",
        "description": "Set up an analytics dashboard to track key performance metrics.",
        "estimated_effort_hours": 40,
        "confidence_level": "Medium",
        "estimated_range_hours": "35-45"
    },
    {
        "task_name": "Optimize Mobile Performance",
        "complexity": "High",
        "size": "Medium",
        "task_type": "Development",
        "description": "Improve mobile performance for better user experience.",
        "estimated_effort_hours": 45,
        "confidence_level": "Medium",
        "estimated_range_hours": "40-50"
    },
    {
        "task_name": "Implement Payment Gateway",
        "complexity": "High",
        "size": "Medium",
        "task_type": "Development",
        "description": "Integrate a payment gateway for secure transactions.",
        "estimated_effort_hours": 50,
        "confidence_level": "Medium",
        "estimated_range_hours": "45-55"
    },
    {
        "task_name": "Conduct Market Analysis",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Marketing",
        "description": "Analyze market trends to inform business strategy.",
        "estimated_effort_hours": 30,
        "confidence_level": "Medium",
        "estimated_range_hours": "25-35"
    },
    {
        "task_name": "Implement SSO",
        "complexity": "High",
        "size": "Medium",
        "task_type": "Development",
        "description": "Integrate single sign-on for enhanced security and user experience.",
        "estimated_effort_hours": 50,
        "confidence_level": "Medium",
        "estimated_range_hours": "45-55"
    },
    {
        "task_name": "Design Email Templates",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Create email templates for marketing campaigns.",
        "estimated_effort_hours": 12,
        "confidence_level": "High",
        "estimated_range_hours": "10-15"
    },
    {
        "task_name": "Setup Firewall",
        "complexity": "High",
        "size": "Medium",
        "task_type": "Infrastructure",
        "description": "Configure firewall settings to protect the network.",
        "estimated_effort_hours": 40,
        "confidence_level": "Medium",
        "estimated_range_hours": "35-45"
    },
    {
        "task_name": "Optimize Search Engine",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Development",
        "description": "Improve the search engine for faster and more accurate results.",
        "estimated_effort_hours": 30,
        "confidence_level": "Medium",
        "estimated_range_hours": "25-35"
    },
    {
        "task_name": "Run Regression Tests",
        "complexity": "High",
        "size": "Large",
        "task_type": "Testing",
        "description": "Execute regression tests to ensure new changes do not affect existing functionality.",
        "estimated_effort_hours": 60,
        "confidence_level": "Medium",
        "estimated_range_hours": "55-65"
    },
    {
        "task_name": "Create Content Strategy",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Marketing",
        "description": "Develop a content strategy to increase user engagement.",
        "estimated_effort_hours": 30,
        "confidence_level": "Medium",
        "estimated_range_hours": "25-35"
    },
    {
        "task_name": "Develop Browser Extension",
        "complexity": "High",
        "size": "Medium",
        "task_type": "Development",
        "description": "Create a browser extension for added functionality.",
        "estimated_effort_hours": 45,
        "confidence_level": "Medium",
        "estimated_range_hours": "40-50"
    },
    {
        "task_name": "Conduct Competitor Analysis",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Marketing",
        "description": "Analyze competitor strategies to identify opportunities.",
        "estimated_effort_hours": 25,
        "confidence_level": "Medium",
        "estimated_range_hours": "20-30"
    },
    {
        "task_name": "Develop Admin Panel",
        "complexity": "High",
        "size": "Large",
        "task_type": "Development",
        "description": "Create an admin panel for managing application content.",
        "estimated_effort_hours": 80,
        "confidence_level": "Medium",
        "estimated_range_hours": "75-85"
    },
    {
        "task_name": "Implement CI Tools",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Infrastructure",
        "description": "Set up continuous integration tools to streamline development.",
        "estimated_effort_hours": 30,
        "confidence_level": "Medium",
        "estimated_range_hours": "25-35"
    },
    {
        "task_name": "Design Brand Guidelines",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Develop brand guidelines to ensure consistency across all channels.",
        "estimated_effort_hours": 20,
        "confidence_level": "High",
        "estimated_range_hours": "15-25"
    },
    {
        "task_name": "Optimize Backend Performance",
        "complexity": "High",
        "size": "Large",
        "task_type": "Development",
        "description": "Enhance backend performance to support higher load.",
        "estimated_effort_hours": 70,
        "confidence_level": "Medium",
        "estimated_range_hours": "65-75"
    },
    {
        "task_name": "Run Usability Testing",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Testing",
        "description": "Conduct usability tests to improve user interface and experience.",
        "estimated_effort_hours": 30,
        "confidence_level": "Medium",
        "estimated_range_hours": "25-35"
    },
    {
        "task_name": "Design Landing Page",
        "complexity": "High",
        "size": "Large",
        "task_type": "Design",
        "description": "Create a visually appealing landing page to attract visitors.",
        "estimated_effort_hours": 40,
        "confidence_level": "Medium",
        "estimated_range_hours": "35-45"
    },
    {
        "task_name": "Create Brand Logo",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Design",
        "description": "Design a unique and memorable logo for the brand.",
        "estimated_effort_hours": 20,
        "confidence_level": "Medium",
        "estimated_range_hours": "15-25"
    },
    {
        "task_name": "Develop Mobile App UI",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Design the user interface for the mobile application.",
        "estimated_effort_hours": 15,
        "confidence_level": "High",
        "estimated_range_hours": "12-18"
    },
    {
        "task_name": "Design Email Newsletter Template",
        "complexity": "High",
        "size": "Medium",
        "task_type": "Design",
        "description": "Create a visually appealing template for email newsletters.",
        "estimated_effort_hours": 30,
        "confidence_level": "Medium",
        "estimated_range_hours": "25-35"
    },
    {
        "task_name": "Create Product Packaging Design",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Design",
        "description": "Design packaging that enhances product appeal and communicates brand identity.",
        "estimated_effort_hours": 25,
        "confidence_level": "Medium",
        "estimated_range_hours": "20-30"
    },
    {
        "task_name": "Design Website Wireframes",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Create wireframes to outline the structure and layout of the website.",
        "estimated_effort_hours": 10,
        "confidence_level": "High",
        "estimated_range_hours": "8-12"
    },
    {
        "task_name": "Create Infographic",
        "complexity": "High",
        "size": "Medium",
        "task_type": "Design",
        "description": "Design an infographic to visually represent complex information.",
        "estimated_effort_hours": 35,
        "confidence_level": "Medium",
        "estimated_range_hours": "30-40"
    },
    {
        "task_name": "Design Social Media Graphics",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Design",
        "description": "Create graphics for social media posts to engage audience.",
        "estimated_effort_hours": 20,
        "confidence_level": "Medium",
        "estimated_range_hours": "15-25"
    },
    {
        "task_name": "Design Poster for Event",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Create an eye-catching poster to promote an event.",
        "estimated_effort_hours": 10,
        "confidence_level": "High",
        "estimated_range_hours": "8-12"
    },
    {
        "task_name": "Create UI Style Guide",
        "complexity": "High",
        "size": "Large",
        "task_type": "Design",
        "description": "Develop a comprehensive style guide for consistent user interface design.",
        "estimated_effort_hours": 50,
        "confidence_level": "Medium",
        "estimated_range_hours": "45-55"
    }
]

infra_data =[
    {
        "task_name": "Design Database Schema",
        "complexity": "High",
        "size": "Large",
        "task_type": "Development",
        "description": "Design the database schema for the new application.",
        "estimated_effort_hours": 30,
        "confidence_level": "Medium",
        "estimated_range_hours": "25-35"
    },
    {
        "task_name": "Implement User Authentication",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Development",
        "description": "Implement user authentication functionality using OAuth 2.0.",
        "estimated_effort_hours": 20,
        "confidence_level": "High",
        "estimated_range_hours": "15-25"
    },
    {
        "task_name": "Write API Documentation",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Documentation",
        "description": "Write comprehensive API documentation for the RESTful endpoints.",
        "estimated_effort_hours": 10,
        "confidence_level": "High",
        "estimated_range_hours": "8-12"
    },
    {
        "task_name": "Upgrade Server RAM",
        "complexity": "Low",
        "size": "Medium",
        "task_type": "Infrastructure",
        "description": "Upgrade the server's RAM to improve system performance.",
        "estimated_effort_hours": 10,
        "confidence_level": "High",
        "estimated_range_hours": "8-12"
    },
    {
        "task_name": "Install Network Firewall",
        "complexity": "Medium",
        "size": "Small",
        "task_type": "Infrastructure",
        "description": "Install and configure a network firewall to enhance security.",
        "estimated_effort_hours": 20,
        "confidence_level": "Low",
        "estimated_range_hours": "15-25"
    },
    {
        "task_name": "Set up Load Balancer",
        "complexity": "High",
        "size": "Large",
        "task_type": "Infrastructure",
        "description": "Set up a load balancer to distribute incoming traffic across multiple servers.",
        "estimated_effort_hours": 40,
        "confidence_level": "Medium",
        "estimated_range_hours": "35-45"
    },
    {
        "task_name": "Configure VPN",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Infrastructure",
        "description": "Configure a virtual private network (VPN) for secure remote access.",
        "estimated_effort_hours": 25,
        "confidence_level": "High",
        "estimated_range_hours": "20-30"
    },
    {
        "task_name": "Optimize Database Queries",
        "complexity": "Medium",
        "size": "Small",
        "task_type": "Infrastructure",
        "description": "Optimize database queries to improve application performance.",
        "estimated_effort_hours": 15,
        "confidence_level": "Medium",
        "estimated_range_hours": "12-18"
    },
    {
        "task_name": "Implement Disaster Recovery Plan",
        "complexity": "High",
        "size": "Large",
        "task_type": "Infrastructure",
        "description": "Develop and implement a disaster recovery plan for critical systems.",
        "estimated_effort_hours": 50,
        "confidence_level": "Low",
        "estimated_range_hours": "40-60"
    },
    {
        "task_name": "Create User Interface Mockups",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Design",
        "description": "Design mockups for the user interface of the application.",
        "estimated_effort_hours": 20,
        "confidence_level": "High",
        "estimated_range_hours": "15-25"
    },
    {
        "task_name": "Review Code for Security Vulnerabilities",
        "complexity": "High",
        "size": "Small",
        "task_type": "Security",
        "description": "Conduct a thorough code review to identify and fix security vulnerabilities.",
        "estimated_effort_hours": 30,
        "confidence_level": "Medium",
        "estimated_range_hours": "25-35"
    },
    {
        "task_name": "Deploy Application to Production Server",
        "complexity": "Low",
        "size": "Large",
        "task_type": "Deployment",
        "description": "Deploy the application to the production server environment.",
        "estimated_effort_hours": 10,
        "confidence_level": "High",
        "estimated_range_hours": "8-12"
    },
    {
        "task_name": "Perform Load Testing",
        "complexity": "Medium",
        "size": "Large",
        "task_type": "Testing",
        "description": "Conduct load testing to assess the performance of the application under high traffic.",
        "estimated_effort_hours": 25,
        "confidence_level": "Medium",
        "estimated_range_hours": "20-30"
    }
]

design_task = [
    {
        "_id": "665371f2cef154a1d321e6f0",
        "task_name": "Design Landing Page",
        "complexity": "Medium",
        "size": "Small",
        "task_type": "Design",
        "description": "Design a landing page for the new product.",
        "estimated_effort_hours": 12,
        "confidence_level": "High",
        "estimated_range_hours": "10-14"
    },
    {
        "_id": "665371f2cef154a1d321e6f1",
        "task_name": "Create Brand Guidelines",
        "complexity": "High",
        "size": "Large",
        "task_type": "Design",
        "description": "Develop comprehensive brand guidelines.",
        "estimated_effort_hours": 45,
        "confidence_level": "Medium",
        "estimated_range_hours": "40-50"
    },
    {
        "_id": "665371f2cef154a1d321e6f2",
        "task_name": "Redesign Mobile App UI",
        "complexity": "High",
        "size": "Medium",
        "task_type": "Design",
        "description": "Redesign the user interface for the mobile app.",
        "estimated_effort_hours": 35,
        "confidence_level": "Medium",
        "estimated_range_hours": "30-40"
    },
    {
        "_id": "665371f2cef154a1d321e6f3",
        "task_name": "Design Print Ads",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Design print advertisements for the campaign.",
        "estimated_effort_hours": 7,
        "confidence_level": "High",
        "estimated_range_hours": "6-8"
    },
    {
        "_id": "665371f2cef154a1d321e6f4",
        "task_name": "Design Brochure",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Design",
        "description": "Create a brochure for the new service.",
        "estimated_effort_hours": 18,
        "confidence_level": "High",
        "estimated_range_hours": "16-20"
    },
    {
        "_id": "665371f2cef154a1d321e6f5",
        "task_name": "Develop Style Guide",
        "complexity": "Low",
        "size": "Large",
        "task_type": "Design",
        "description": "Develop a style guide for the company's visual identity.",
        "estimated_effort_hours": 22,
        "confidence_level": "Medium",
        "estimated_range_hours": "20-24"
    },
    {
        "_id": "665371f2cef154a1d321e6f6",
        "task_name": "Design Website Icons",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Create custom icons for the website.",
        "estimated_effort_hours": 6,
        "confidence_level": "High",
        "estimated_range_hours": "5-7"
    },
    {
        "_id": "665371f2cef154a1d321e6f7",
        "task_name": "Create Email Templates",
        "complexity": "Medium",
        "size": "Small",
        "task_type": "Design",
        "description": "Design email templates for marketing campaigns.",
        "estimated_effort_hours": 10,
        "confidence_level": "High",
        "estimated_range_hours": "8-12"
    },
    {
        "_id": "665371f2cef154a1d321e6f8",
        "task_name": "Design Conference Booth",
        "complexity": "High",
        "size": "Large",
        "task_type": "Design",
        "description": "Design the layout and visuals for the conference booth.",
        "estimated_effort_hours": 50,
        "confidence_level": "Medium",
        "estimated_range_hours": "45-55"
    },
    {
        "_id": "665371f2cef154a1d321e6f9",
        "task_name": "Redesign Company Newsletter",
        "complexity": "Low",
        "size": "Medium",
        "task_type": "Design",
        "description": "Redesign the monthly company newsletter.",
        "estimated_effort_hours": 15,
        "confidence_level": "High",
        "estimated_range_hours": "13-17"
    },
    {
        "_id": "665371f2cef154a1d321e6fa",
        "task_name": "Create Infographics for Blog",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Design",
        "description": "Design infographics to accompany blog posts.",
        "estimated_effort_hours": 20,
        "confidence_level": "High",
        "estimated_range_hours": "18-22"
    },
    {
        "_id": "665371f2cef154a1d321e6fb",
        "task_name": "Develop Product Packaging",
        "complexity": "High",
        "size": "Large",
        "task_type": "Design",
        "description": "Create packaging designs for the new product line.",
        "estimated_effort_hours": 48,
        "confidence_level": "Medium",
        "estimated_range_hours": "43-53"
    },
    {
        "_id": "665371f2cef154a1d321e6fc",
        "task_name": "Design Annual Report",
        "complexity": "High",
        "size": "Medium",
        "task_type": "Design",
        "description": "Design the annual report for stakeholders.",
        "estimated_effort_hours": 30,
        "confidence_level": "Medium",
        "estimated_range_hours": "25-35"
    },
    {
        "_id": "665371f2cef154a1d321e6fd",
        "task_name": "Design Presentation Templates",
        "complexity": "Medium",
        "size": "Small",
        "task_type": "Design",
        "description": "Create templates for company presentations.",
        "estimated_effort_hours": 12,
        "confidence_level": "High",
        "estimated_range_hours": "10-14"
    },
    {
        "_id": "665371f2cef154a1d321e6fe",
        "task_name": "Redesign Social Media Profiles",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Update the design of social media profile pages.",
        "estimated_effort_hours": 8,
        "confidence_level": "High",
        "estimated_range_hours": "7-9"
    },
    {
        "_id": "665371f2cef154a1d321e6ff",
        "task_name": "Create Mobile App Wireframes",
        "complexity": "Medium",
        "size": "Large",
        "task_type": "Design",
        "description": "Develop wireframes for the new mobile app.",
        "estimated_effort_hours": 25,
        "confidence_level": "High",
        "estimated_range_hours": "22-28"
    },
    {
        "_id": "665371f2cef154a1d321e700",
        "task_name": "Design Event Invitations",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Design invitations for the upcoming event.",
        "estimated_effort_hours": 5,
        "confidence_level": "High",
        "estimated_range_hours": "4-6"
    },
    {
        "_id": "665371f2cef154a1d321e701",
        "task_name": "Design Interactive Prototypes",
        "complexity": "High",
        "size": "Medium",
        "task_type": "Design",
        "description": "Create interactive prototypes for user testing.",
        "estimated_effort_hours": 35,
        "confidence_level": "Medium",
        "estimated_range_hours": "30-40"
    },
    {
        "_id": "665371f2cef154a1d321e702",
        "task_name": "Develop Visual Content for Ads",
        "complexity": "Medium",
        "size": "Large",
        "task_type": "Design",
        "description": "Design visual content for online and print ads.",
        "estimated_effort_hours": 28,
        "confidence_level": "High",
        "estimated_range_hours": "25-31"
    },
    {
        "_id": "665371f2cef154a1d321e703",
        "task_name": "Design Product Catalog",
        "complexity": "High",
        "size": "Large",
        "task_type": "Design",
        "description": "Create a product catalog for the new line.",
        "estimated_effort_hours": 45,
        "confidence_level": "Medium",
        "estimated_range_hours": "40-50"
    },
    {
        "_id": "665371f2cef154a1d321e6e7",
        "task_name": "Design UI Mockups",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Create UI mockups for the new application interface.",
        "estimated_effort_hours": 10,
        "confidence_level": "High",
        "estimated_range_hours": "8-12"
    },
    {
        "_id": "665371f2cef154a1d321e6e8",
        "task_name": "Create High-Fidelity Prototypes",
        "complexity": "High",
        "size": "Large",
        "task_type": "Design",
        "description": "Develop high-fidelity prototypes for the project.",
        "estimated_effort_hours": 40,
        "confidence_level": "Medium",
        "estimated_range_hours": "35-45"
    },
    {
        "_id": "665371f2cef154a1d321e6e9",
        "task_name": "Design Marketing Materials",
        "complexity": "Medium",
        "size": "Medium",
        "task_type": "Design",
        "description": "Design marketing materials for the upcoming campaign.",
        "estimated_effort_hours": 20,
        "confidence_level": "High",
        "estimated_range_hours": "18-22"
    },
    {
        "_id": "665371f2cef154a1d321e6ea",
        "task_name": "Redesign Website Layout",
        "complexity": "High",
        "size": "Medium",
        "task_type": "Design",
        "description": "Redesign the layout of the company website.",
        "estimated_effort_hours": 25,
        "confidence_level": "Medium",
        "estimated_range_hours": "20-30"
    },
    {
        "_id": "665371f2cef154a1d321e6eb",
        "task_name": "Design New Logo",
        "complexity": "Low",
        "size": "Small",
        "task_type": "Design",
        "description": "Create a new logo for the company.",
        "estimated_effort_hours": 5,
        "confidence_level": "High",
        "estimated_range_hours": "4-6"
    },
    {
        "_id": "665371f2cef154a1d321e6ec",
        "task_name": "Develop Mobile App UI",
        "complexity": "Medium",
        "size": "Large",
        "task_type": "Design",
        "description": "Design the user interface for the mobile application.",
        "estimated_effort_hours": 30,
        "confidence_level": "Medium",
        "estimated_range_hours": "25-35"
    },
    {
        "_id": "665371f2cef154a1d321e6ed",
        "task_name": "Create Infographic",
        "complexity": "Low",
        "size": "Medium",
        "task_type": "Design",
        "description": "Design an infographic for the new product launch.",
        "estimated_effort_hours": 15,
        "confidence_level": "High",
        "estimated_range_hours": "12-18"
    },
    {
        "_id": "665371f2cef154a1d321e6ee",
        "task_name": "Design E-commerce Platform",
        "complexity": "High",
        "size": "Large",
        "task_type": "Design",
        "description": "Design the user interface and experience for the new e-commerce platform.",
        "estimated_effort_hours": 50,
        "confidence_level": "Medium",
        "estimated_range_hours": "45-55"
    },
    {
        "_id": "665371f2cef154a1d321e6ef",
        "task_name": "Design Social Media Graphics",
        "complexity": "Medium",
        "size": "Small",
        "task_type": "Design",
        "description": "Create graphics for social media campaigns.",
        "estimated_effort_hours": 8,
        "confidence_level": "High",
        "estimated_range_hours": "7-9"
    }
]

    



# print(tasks_data)
# print(task_design)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client['estimation']
Historical_data = db["Historical_data"]

# Insert task data into MongoDB
try:
    for task in design_task:
        Historical_data.insert_one(task)
    print(f"{len(design_task)} tasks inserted successfully.")
except Exception as e:
    print(f"Error: {e}")

