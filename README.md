# PC Part Picker

Welcome to PC Part Picker! This repository hosts an interactive Python application designed to help users build their own custom PC configurations or select from a variety of prebuilt options. With PC Part Picker, users can explore a wide range of components such as CPUs, motherboards, GPUs, RAM, storage, power supplies, and cases, and create their ideal PC configuration based on their budget and preferences.

The application provides a user-friendly interface that allows users to make component selections, calculate the total price of their configurations, and even save and search for their custom builds. Additionally, users can choose from a selection of prebuilt PC configurations to find the perfect fit for their needs.

Whether you're a PC enthusiast looking to build your dream rig or a user seeking a prebuilt solution, PC Part Picker is here to assist you in making informed decisions about your PC hardware.


## Table of Contents

  - [Table of Contents](#table-of-contents)
  - [Features](#features)
    - [Future Enhancements](#future-enhancements)
  - [UX/UI Design](#ux-design)
  - [Technologies Used](#technologies-used)
  - [Testing](#testing)
    - [User Stories](#user-stories)
  - [Issues Fixed](#issues-fixed)
  - [Manual Testing](#manual-testing)
  - [Validators Used](#validators-used)
  - [Deployment](#deployment)
    - [Codeanwhere](#codeanywhere)
  - [Run code locally](#run-code-locally)
  - [Cloning](#cloning)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
  - [Acknowledgements](#acknowledgements)


## Features

### Main Menu

Upon launching the application, users are greeted with a main menu that offers several options:

1. **Build a PC**: This option allows users to create their own custom PC configuration by selecting individual components such as CPU, motherboard, GPU, RAM, storage, power supply, and case. The app guides users through the process of selecting components and calculates the total price of the configuration.

2. **Prebuilt PCs**: Users can choose from a selection of prebuilt PC configurations that fit specific budget ranges. The available options include configurations "Under $1000" and "Under $2000." This feature helps users quickly explore preconfigured options that meet their budget and performance requirements.

3. **Search Builds by Name**: Users can search for previously saved custom builds using either the build name or configuration description. This feature is helpful for users who want to revisit and review their previous configurations.

4. **Exit**: This option allows users to exit the application.
    

### Build a PC

 When users choose the "Build a PC" option, they are guided through the process of selecting individual components for their custom configuration:

- **CPU**: Users can choose a CPU from a list of available options. Each CPU is accompanied by its model name and price.

- **Motherboard**: Similar to CPU selection, users can choose a compatible motherboard for their selected CPU.

- **GPU**: Users can select a graphics processing unit (GPU) based on their preferences and performance needs.

- **RAM**: Users can choose the amount and type of RAM for their configuration.

- **Storage**: Users can select the storage device, such as an SSD or HDD, based on their storage requirements.

- **Power Supply**: Users can choose a power supply unit (PSU) suitable for their configuration.

- **Case**: Users can select a computer case that accommodates their chosen components.

    Once all components are selected, the app calculates and displays the total price of the configuration. Users have the option to publish the build by providing a name for it.

### Prebuilt PCs

This option presents users with two budget-friendly prebuilt configurations:

  **Under $1000**: Users can view a preconfigured PC build designed to cost under $1000. This option is suitable for budget-conscious users seeking a well-balanced setup.

  **Under $2000**: Users interested in a higher-performance configuration can explore a prebuilt option designed to cost under $2000.

Users can select either prebuilt option to view the detailed components and their total price.

### Search Builds by Name

    Users can search for and retrieve previously saved custom builds using the build name or configuration description. This feature allows users to find and review their past configurations for reference or modification.

### Exit

    The "Exit" option allows users to gracefully exit the application when they are done exploring and building configurations.

The PC Part Picker app provides users with an intuitive and interactive experience, helping them make informed decisions about their PC hardware components based on their preferences and budget. Whether users are building a gaming rig, a workstation, or a general-purpose PC, the app assists in creating the perfect configuration.


### Future Enhancements

In this section of the README, you can mention potential future enhancements or features that you plan to add to the PC Part Picker app. These enhancements might include:

   **User Accounts**: Implementing user accounts could allow users to save their configurations and access them across different sessions or devices.

   **Component Compatibility Check**: Adding a compatibility check feature that ensures selected components are compatible with each other could help users avoid compatibility issues.

   **Component Reviews**: Integrating component reviews and ratings could provide users with additional insights before making their selections.

   **Price Tracking**: Offering price tracking functionality to notify users of price drops or deals on their selected components.

   **Comparison Tool**: Creating a comparison tool that allows users to compare multiple configurations side by side.

   **Export and Sharing**: Enabling users to export their configurations or share them with others through URLs or social media.


## UX/UI Design

## Technologies Used

The PC Part Picker app was developed using a combination of programming languages, frameworks, and tools. Here is a list of the key technologies used in the development process:

**Python**: The core logic of the application, including user interactions and data processing, was implemented using the Python programming language.

**Google Sheets API**: The app leverages the Google Sheets API to read and write data to Google Sheets, allowing users to select components, save builds, and retrieve information.

**gspread**: The gspread library was used to interact with the Google Sheets API in Python, enabling seamless communication between the app and the Google Sheets spreadsheets.

**Google OAuth**: The app utilizes Google OAuth 2.0 for secure user authentication and authorization to access Google Sheets data.

**CodeAnywhere**: The development environment was set up and managed using CodeAnywhere, providing an online platform for coding, testing, and collaboration.

**Heroku**: The PC Part Picker app was deployed using Heroku, a cloud platform that allows applications to be hosted and accessible online.


## Testing

The PC Part Picker app underwent thorough testing to ensure that it functions correctly, provides accurate information, and delivers a seamless user experience. The testing process involved the following aspects:

### User Stories

    The app's functionality was tested against a set of user stories to verify that it meets the expected requirements and provides a satisfactory user experience. Some examples of user stories and their testing outcomes include:

1. As a PC enthusiast, I want to be able to explore a variety of components to build my ideal custom PC configuration.

2. As a budget-conscious user, I want to view prebuilt PC configurations within specific price ranges to quickly find options that fit my budget.

3. As a user, I want to be able to search for previously saved custom builds by their names or configuration descriptions for easy reference.

4. As a gaming enthusiast, I want to be able to select a powerful graphics processing unit (GPU) to ensure optimal gaming performance in my PC build.

5. As a content creator, I want to choose a CPU with high processing power and a large amount of RAM to handle resource-intensive tasks efficiently.

6. As a user with specific brand preferences, I want to be able to filter components by brand to ensure compatibility and consistency in my PC build.

7. As a user, I want to calculate the total price of my selected components to ensure they fit within my allocated budget.

8. As a first-time PC builder, I want the application to guide me through the process of selecting compatible components for my PC configuration.

9. As a user, I want to save my custom PC configurations for future reference, modification, or comparison with other builds.

10. As a user, I want to receive accurate information about the components, including their model names, prices, and specifications.

11. As a user, I want to exit the application gracefully when I'm done exploring configurations or building a PC.

## Issues Fixed

| Issues  |                              | Fixed  |
| ---     |                              |  ---   |


## Manual Testing

Manual testing was performed to ensure the accuracy of calculations, proper display of information, and seamless navigation through the app's menu options. The testing covered scenarios such as:

- Selecting different components and ensuring their prices are accurately calculated in the total price.
- Choosing various prebuilt configurations to verify that the correct details are displayed.
- Searching for builds by name and checking if the matching builds are accurately presented.
- Exiting the app to make sure it works as intended
  
## Validators Used

[CI Python Linter](https://pep8ci.herokuapp.com/#)

## Deployment

The PC Part Picker app was successfully deployed using two key technologies: CodeAnywhere and Heroku.

### Heroku

Heroku is a popular cloud platform that allows you to host web applications. To deploy the PC Part Picker app on Heroku, follow these steps:

1. [Sign up](https://signup.heroku.com/) for a Heroku account if you don't already have one.

2. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) on your local machine.

3. Open a terminal and navigate to your PC Part Picker project directory.

4. Log in to Heroku using the command: `heroku login`.

5. Initialize a Git repository in your project directory (if not already initialized) with `git init`.

6. Create a `requirements.txt` file that lists the Python dependencies for your app. You can generate this file by running `pip freeze > requirements.txt`.

7. Create a `Procfile` (without any file extension) in your project directory. The Procfile should contain the following line, which tells Heroku how to run your app: `web: python your_app_filename.py`.

8. Commit your changes and push them to a Git repository on Heroku using the following commands:
   ```bash
   git add .
   git commit -m "Initial deployment to Heroku"
   heroku create your-app-name
   git push heroku master

### Codeanywhere

CodeAnywhere is an online development environment that you can use to code and deploy your PC Part Picker app. Here's how to deploy it on CodeAnywhere:

1. Sign up for a CodeAnywhere account if you don't already have one.

2. Create a new workspace in CodeAnywhere.

3. Clone your PC Part Picker project repository into your CodeAnywhere workspace.

4. Set up any environment variables or configurations required for your app.

5. Install any necessary Python dependencies.

6. Run your PC Part Picker app within the CodeAnywhere environment.

7. You can access your app using the provided URL.

## Run code locally

There is different approaches should you choose to use GitPod to clone the project, or a different IDE.

- Use web browser -- google -- firefox etc.
- Login to your github account or sign up if you haven't.
- Install the gitpod extenstion for your browser.
- In github find the repository.
- Click on gitpod button.
- New workspace will open containing the project code.

## Cloning

1. Navigate to the github repository.
2. Choose the dropdown on the code button.
3. Open your IDE and terminal.
4. Set the working directory to location.
5. Type in "git clone" followed by the URL. Make sure to include a space after git clone for the url,   press enter.
6. Project created.
For more information on
[GitHub](https://docs.github.com/en)


## Credits

### Content

- [Code Institute Solutions - README Template](https://github.com/Code-Institute-Solutions/readme-template)

  
### Media



## Acknowledgements

- Student Support.
- Mitko Bachvarov Mentor.
