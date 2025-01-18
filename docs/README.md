---
layout: home
permalink: index.html

# Please update this with your repository name and title
repository-name: e18-4yp-RPA-attacks-using-Machine-Learning-Algorithms
title: RPA Attacks using Machine Learning Algorithms
---

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template"

# RPA Attacks using Machine Learning Algorithms

#### Team

- E/18/028, Jeewantha Ariyawansha, [e18028@eng.pdn.ac.lk](mailto:name@email.com)
- E/18/173, Ishan Kasthuripitiya, [e18173@eng.pdn.ac.lk](mailto:name@email.com)
- E/18/285, Tharindu Ranasinghe, [e18285@eng.pdn.ac.lk](mailto:name@email.com)

#### Supervisors

- Assoc. Prof. Manjula Sandirigama, [manjula.sandirigama@eng.pdn.ac.lk](mailto:name@eng.pdn.ac.lk)
- Dr. Darshana Jayasinghe, [darshana.jayasinghe@sydney.edu.au](mailto:name@eng.pdn.ac.lk)

#### Table of content

1. [Abstract](#abstract)
2. [Related works](#related-works)
3. [Methodology](#methodology)
4. [Publications](#publications)
5. [Links](#links)


---

<!-- 
DELETE THIS SAMPLE before publishing to GitHub Pages !!!
This is a sample image, to show how to add images to your page. To learn more options, please refer [this](https://projects.ce.pdn.ac.lk/docs/faq/how-to-add-an-image/)
![Sample Image](./images/sample.png) 
-->


## Abstract
This project aims to investigate the use of machine learning algorithms to enhance remote power analysis attacks (RPAAs) on cryptographic systems. RPAAs are a type of side-channel attack that exploit the power consumption patterns of a target device to extract secret information, such as keys, without physical access. Machine learning algorithms can improve the accuracy and efficiency of RPAAs by reducing the data requirements, adapting to different scenarios, and overcoming noise and countermeasures. This project reviews the state-of-the-art methods for RPAAs using machine learning, including supervised learning techniques such as regression, classification, and ensemble methods. It also discusses the challenges, benefits, and ethical issues of applying machine learning to RPAAs, as well as the potential countermeasures and future research directions. The project is based on the AISY framework, which provides a flexible and adaptive platform for side-channel analysis using information-theoretic metrics.

## Related works

#### 1. Side Channel Attacks
Side Channel Attacks(SCA) utilize the information poured during the computation process. The side-channel attacks target the security of the cryptographic devices with alarming efficiency. SCA attacks use power consumption information from the cryptosystem to extract the secret key stored in the cryptosystem, thus effectively breaking the cryptosystem[1].
The Side Channel Attacks can be classified at three levels: Actions over the computation process, accessing the modules, and methods used in the analysis process. Actions over computation processes can be classified as passive attacks and active attacks.
<br/>
<b>1. Passive attacks</b> are based on observing side-channel information, such as the chip's power consumption. This is used to gain information on the operation handled by the attackers.
<br/>
<b>2. Active attacks:</b> The active attack consists of perturbing the chip processing to obtain abnormal behavior. With the help of information, the attackers can alter the originality. 

#### 2. Remote Power Analysis Attacks
Remote Power Analysis Attacks (RPAAs) involve analyzing a cryptographic device’s power usage remotely to extract sensitive information, such as secret keys. These attacks exploit power consumption patterns and pose a significant threat to cryptographic systems. Countermeasures must be implemented at multiple levels, such as hardware design, cryptographic algorithms, and protocol implementations, to mitigate the risk of RPAAs. Furthermore, current research focuses on creating protection and detection systems to efficiently identify and stop threats using remote power analysis.

#### 3. RPA Attacks on FPGAs
In this work, it is demonstrated that the programmable resources of an FPGA can be utilized to perform side-channel attacks. Internal sensors based on programmable primitives are developed, and the internally measured side-channel leakages are transferred outside. Distributed and calibrated delay sensors capable of indirectly measuring voltage fluctuations due to power consumption are introduced. Different settings and parameters for the employed sensors are presented using a cryptographic core as a case study. Practical key-recovery attacks are exhibited using their side-channel measurements, confirming the applicability of the underlying measurement methodology.This opens a new door to integrate hardware Trojans in
 
a) Applications where the FPGA is remotely accessible, such as in the cloud, and 

b) Multi-tenant FPGAs, where the reconfigurable resources are shared among different users. This type of attack is highly difficult to detect since there is no signal connection between the targeted (cryptographic) core and the internally deployed sensors.

#### 4. On-chip power analysis attacks
The integration of voltage sensors on chips has become pivotal for tracking voltage levels, impacting circuit performance and power consumption. Recent advancements include FPGA-based internal sensors for detecting side-channel leakages, facilitating easier extraction and transmission of data. However, multi-user FPGA environments present security concerns, as studies show potential for remote Side Channel Attacks. Software-induced hardware attacks further compound these risks, leveraging network connections for exploitation. Various methodologies, such as VITI, PPWM, RDS, and LUTSensor, are compared in terms of effectiveness and adaptability for side-channel assaults. Detecting power attacks in real-time is proposed through statistical analysis of on-chip voltage variations, offering a proactive defense mechanism. Additionally, guidelines for securing power delivery against power analysis attacks are suggested, emphasizing the importance of monitoring power distribution networks and sensor placement. Remote power analysis attacks pose significant threats, requiring countermeasures like constant-time algorithms and trusted firmware updates to mitigate risks effectively.

#### 5. Machine Learning on Side Channel Attack
Scholars have extensively explored the use of machine learning techniques in side-channel attacks, which exploit unintended data leakage from cryptographic implementations. Traditional statistical methods and machine learning algorithms like Least Square Support Vector Machines (LS-SVMs) have been employed for this purpose. However, recent advancements have seen the emergence of deep learning-based profiling techniques, offering more accurate and resilient attack strategies, particularly in template attacks. Deep learning methods, such as Support Vector Machines (SVM), Random Forest (RF), and novel strategies, have shown promise in improving attack accuracy by maximizing the Perceived Information (PI) during neural network training. Among various paradigms, AISY (Adaptive Information-theoretic Side-channel Analysis) stands out for its flexibility and comprehensive framework, outperforming alternatives like ASCAD and SCAML. AISY's adaptive nature and focus on information-theoretic metrics ensure precise and effective attacks, making it a valuable tool for enhancing security evaluations of cryptographic devices.

## Methodology
![image](https://github.com/cepdnaclk/e18-4yp-RPA-attacks-using-Machine-Learning-Algorithms/assets/73388062/7d1a35c1-d187-449f-ad4b-4e8e98b77208)

#### Data collection - Power Analysis
+ AES is implemented on Field Programmable Gate Array (FPGA) with key.
+ Build a TDC sensor on FPGA to measure power dissipation.
+ Time to Digital Converter (TDC) is logical function that used for measuring small voltage fluctuation.
+ Measuring power dissipation using different key combinations.

#### Attack Execution
+ Try random key-byte combinations.
+ Attacks using the Hamming Distance model
![image](https://github.com/cepdnaclk/e18-4yp-RPA-attacks-using-Machine-Learning-Algorithms/assets/73388062/2c225db6-f469-4937-90d8-e3bc7bd998be)

#### Result Evaluation
+ Evaluation Metrics
  + Guessing Entropy
  + Success rate

+ Feed data into different machine learning algorithms.
+ Monitoring guessing entropy and success rate.

<b> Success rate can be used, </b>
+ Execute attacks n times using data
+ Count successful guesses

<!-- ## Experiment Setup and Implementation

## Results and Analysis

## Conclusion -->

## Publications
[//]: # "Note: Uncomment each once you uploaded the files to the repository"

1. [Semester 7 report](https://docs.google.com/document/d/1YkaQz3yMLTlM7Aq03VCak5XpC2KUOVYfIIlntpxleoM/edit?usp=sharing)
2. [Semester 7 slides](https://www.canva.com/design/DAF-GgL5M-s/xHTKBkTzQByJPB7T3HfwiQ/edit?utm_content=DAF-GgL5M-s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
<!-- 3. [Semester 8 report](./) -->
<!-- 4. [Semester 8 slides](./) -->
<!-- 5. Author 1, Author 2 and Author 3 "Research paper title" (2021). [PDF](./). -->


## Links

[//]: # ( NOTE: EDIT THIS LINKS WITH YOUR REPO DETAILS )

- [Project Repository](https://github.com/cepdnaclk/e18-4yp-RPA-attacks-using-Machine-Learning-Algorithms)
- [Project Page](https://cepdnaclk.github.io/e18-4yp-RPA-attacks-using-Machine-Learning-Algorithms)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)

[//]: # "Please refer this to learn more about Markdown syntax"
[//]: # "https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet"
