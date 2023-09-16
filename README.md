# Django Web Apps

This repository contains a collection of Django web applications that replicate simplified versions of popular websites and services.

## Table of Contents

- [Introduction](#introduction)
- [Applications](#applications)
- [Getting Started](#getting-started)

## Introduction

These Django web applications serve as educational projects and demonstrate how to build simplified versions of well-known websites and services using Django, a high-level Python web framework. Each application is designed to showcase various Django features and best practices in web development.

## Applications

Here are the web applications included in this repository:

1. **Wikipedia Clone:** A simplified version of Wikipedia, allowing users to browse and create articles.
2. **Google Search Clone:** A basic search engine that allows users to perform web searches.
3. **Facebook Clone:** A simplified version of a social networking platform with user profiles and posts.
4. **E-commerce Store:** A basic e-commerce website for buying and selling products.
5. **E-mail Client:** A simple email client for sending, receiving, storing, and searching for users' emails.
6. **Auction Platform:** A basic online auction platform for buying and selling items.

Each application is organized in its respective subdirectory within this repository.

## Getting Started

To run any of these web applications locally, follow these steps:

   Clone this repository to your local machine:
   ```bash
    # Clone this repository to your local machine
    git clone https://github.com/justinjmilner/Web-Development-Projects.git

    # Navigate to the project directory
    cd Web-Development-Projects

    # Create a virtual environment (optional but recommended)
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate

    # Install the project's dependencies
    pip install -r requirements.txt

    # Apply database migrations
    python manage.py migrate

    # Start the development server
    python manage.py runserver

