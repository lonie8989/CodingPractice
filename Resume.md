%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Deedy - One Page Two Column Resume
% LaTeX Template
% Version 1.2 (16/9/2014)
%
% Original author:
% Debarghya Das (http://debarghyadas.com)
%
% Original repository:
% https://github.com/deedydas/Deedy-Resume
%
% IMPORTANT: THIS TEMPLATE NEEDS TO BE COMPILED WITH XeLaTeX
%
% This template uses several fonts not included with Windows/Linux by
% default. If you get compilation errors saying a font is missing, find the line
% on which the font is used and either change it to a font included with your
% operating system or comment the line out to use the default font.
% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% TODO:
% 1. Integrate biber/bibtex for article citation under publications.
% 2. Figure out a smoother way for the document to flow onto the next page.
% 3. Add styling information for a "Projects/Hacks" section.
% 4. Add location/address information
% 5. Merge OpenFont and MacFonts as a single sty with options.
% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% CHANGELOG:
% v1.1:
% 1. Fixed several compilation bugs with \renewcommand
% 2. Got Open-source fonts (Windows/Linux support)
% 3. Added Last Updated
% 4. Move Title styling into .sty
% 5. Commented .sty file.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Known Issues:
% 1. Overflows onto second page if any column's contents are more than the
% vertical limit
% 2. Hacky space on the first bullet point on the second column.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\documentclass[]{deedy-resume-openfont}
\usepackage{fancyhdr}
 
\pagestyle{fancy}
\fancyhf{}
 
\begin{document}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%     LAST UPDATED DATE
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\lastupdated

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%     TITLE NAME
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\namesection{Namgi}{Yoon}{ \urlstyle{same}
Phone: 801-707-8399 | \href{mailto:namgi.yoon22@gmail.com}{namgi.yoon22@gmail.com} |
\href{https://www.linkedin.com/in/ngyoon}{linkedin.com/in/ngyoon}
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%     COLUMN ONE
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{minipage}[t]{0.33\textwidth} 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     EDUCATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Education} 

\subsection{University of Utah}
\descript{BS in Computer Science}
\location{Aug 2011 - May 2016 | Salt Lake City}
\sectionsep

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     COURSEWORK
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Coursework}

\subsection{Undergraduate}
Alg \& Data Struct \\
Object-Oriented Prog \\
Operating Systems \\
Computer Networks \\
Software Engineering \\
Database system \\
\sectionsep

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     SKILLS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Skills}
\subsection{Languages}
C\# \textbullet{}   Python \textbullet{} Typescript \textbullet{} JavaScript \\
SQL \textbullet{}  YAML

\hfill\\

\subsection{Frameworks}
.NET Core \textbullet{} EF Core \textbullet{} Angular \textbullet{} Ionic 4

\hfill\\

\subsection{Cloud Services}
API Gatway \textbullet{} Lambda \textbullet{} OpenSearch \textbullet{} SNS \textbullet{}
Beanstalk \textbullet{} IAM \textbullet{} Firebase

\hfill\\

\subsection{Databases}
MySQL \textbullet{} MSSQL \textbullet{} Mongodb \\

\hfill\\

\subsection{Others}
Linux \textbullet{} Node.js \textbullet{} Docker \textbullet{} Kubernetes \textbullet{}
Git \textbullet{} Gitlab \textbullet{} Jenkins \textbullet{} Ansible \textbullet{} Crontab \textbullet{}
RabbitMQ \textbullet{} Redis \textbullet{} OAuth2.0 \textbullet{} RESTful API \textbullet{} Agile \textbullet{} Xunit \textbullet{} Puppeteer \textbullet{} DevExpress
\sectionsep

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     INTEREST
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Interest}
Clean Architecture \\
Distributed Systems \\
Cloud Computing \\
Machine Learning \\
\sectionsep

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%     COLUMN TWO
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\end{minipage} 
\hfill
\begin{minipage}[t]{0.66\textwidth} 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     PROFESSIONAL EXPERIENCE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Professional Experience}
\runsubsection{11 Health \& Tech}
\descript{| Full Stack Developer }
\location{Apr 2021 - Present | Irvine, CA}
\vspace{\topsep} % Hacky fix for awkward extra vertical space
\begin{tightemize}
\item Designed \& migrated data pipelines of medical device sales order for 11 Heath.
\item Led an initiative to build gateway app to transmit sensor data into Databases.
\item Built simulator app to deliver data in database for ML team.
\item Developed reporting system to convert arbitrary pages to PDF in .NET apps.
\item Implemented new patient on-boarding page in admin portal web app.
\item Improved metric monitoring system to patient activity data using AWS.
\item Improved CI/CD pipeline on Jenkins on AWS to automate release process.
\item Collaborate with third party software teams and internal teams on agile scrum methodology.
\end{tightemize}
\sectionsep

\runsubsection{Protrend LTD}
\descript{| Junior Software Developer }
\location{Nov 2018 – Dec 2020 | Commerce, CA}
\begin{tightemize}
\item Built production lines system for garment wholesale from scratch and continually implement new features by the client request.
\item Reduced IT expanses and labor fee 30\% migrated on-promised servers to AWS.
\end{tightemize}
\sectionsep

\runsubsection{Woongjin, Inc}
\descript{| .NET Developer }
\location{Aug 2017 – Now 2018 | Buena Park, CA}
\begin{tightemize}

\item Implemented data access transaction after analysis of EDI 810 and EDI 850.
\item Implemented web applications: CJF Sales Force, KUMHO and HANWHA.
\item Maintained internal HR web application for Woongjin Inc using PHP.
\end{tightemize}
\sectionsep

\runsubsection{SGS Networks, Inc}
\descript{| Entry .Net Developer }
\location{Aug 2016 – Now 2017 | Los Angeles, CA}
\begin{tightemize}
\item Designed +20 object oriented design about accounting \& sales module for garment industry.
\end{tightemize}
\sectionsep

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     SIDE WORK & PROJECT
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Side Work}
\runsubsection{Stanleyprep ERP}
\descript{| Software Developer}
\location{Ang 2019 - Apr 2020}
Goal of the side work was managing study abroad programs admissions for Stanleyprep. Designed the system from scratch and tech specs - frontend: Angular 8, backend: .NET Core 3.1. Implemented dev tools to reduce development time more than 50\% by Angular Schematics. Used OAuth 2.0 \& OpenId used for authorization protocols. Used CI/CD in gitlab.
\sectionsep

\runsubsection{PickEatUp - Android, iOS and Web}
\descript{| Software Developer}
\location{May 2020 - Nov 2020}
Goal of the project was building contactless food ordering service for store and customer. Developed mobile applications using Ionic 4 framework. Applied Kubernetes multi clusters, HAproxy, and Multi-Master Replication Manager(MMM) on MySql for reliability and scalability.
\textbf{\href{https://play.google.com/store/apps/developer?id=RENDERCORE+LAB+INC&hl=en_US&gl=US}{(Android app link)}}
\textbf{\href{https://www.pickeatup.net/home}{(Web app link)}}
\sectionsep

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     CERTIFICATIONS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{CERTIFICATIONS} 
\begin{tabular}{rll}
2014	 & Coursera  & Convolutional Neural Networks \\
2014	 & Coursera  & Neural Networks and Deep Learning \\
2011     & Cicso & Cisco Certified Network Associate \\
\end{tabular}
\sectionsep

\end{minipage} 
\end{document}  \documentclass[]{article}
