# XMLBrute
### A program made for brute-forcing WordPress logins using XMLRPC


<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

## DISCLAIMER

The developer of this program is not responsible for any damages caused by the consumer's use of the program, including any immoral or unethical actions or consequences thereof.

<!-- ABOUT THE PROJECT -->
## About The Project

This is a program made to brute force passwords on wordpress logins using XMLRPC. <br> 
Note: This is more of a Proof-of-Concept as brute-forcing an account password would take a long time. <br> This will work only if the password is weak enough or the wordlist has that password in it.



### Built With

* [![Python][Python.org]][Python-url]



<!-- GETTING STARTED -->
## Getting Started

All that's needed is to clone the repo or download a ZIP copy, then run the xmlrpcbrute.py with python and go through the steps.

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/GuardianN06/XMLBrute.git
   ```
   
2. Change directory to that folder
    ```sh
    cd XMLBrute
    ```
3. Then just run the python program
    ```sh
    python xmlrpcbrute.py
    ```


<!-- USAGE EXAMPLES -->
## Usage

You input the link of the xmlrpc endpoint, you input the username, a wordlist (preferably shorter) and the amount of threads (5 is recommended). <br> How you get the username is you do https://site.com/wp-json/wp/v2/users and this should supply you with a json format text. From that json, you should look for a variable after the "slug" object which is the username. Note, there can be multiple usernames on a single wordpress install.



https://github.com/GuardianN06/XMLBrute/assets/104389989/88b6d0ca-689b-4d2f-abec-82301ccf1546



<p align="right">(<a href="#readme-top">back to top</a>)</p>


[Python.org]: https://img.shields.io/badge/python.org-000000?style=for-the-badge&logo=python
[Python-url]: https://python.org/
