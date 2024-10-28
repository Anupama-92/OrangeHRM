pipeline {
    agent any  // The pipeline can run on any available Jenkins agent

    environment {
        // Define environment variables if needed (e.g., paths to drivers, credentials, etc.)
        WORKSPACE = "${env.WORKSPACE}"
        REPORT_PATH = "reports"
        SCREENSHOTS_PATH = "screenshots"
    }

    stages {
        // Stage 1: Checkout the source code from GitHub or any other SCM
        stage('Checkout') {
            steps {
                git 'https://your-repo-url.git'
            }
        }

        // Stage 2: Install dependencies (e.g., selenium, pytest, etc.)
        stage('Install Dependencies') {
            steps {
                script {
                    // Install required packages for the Selenium framework
                    if (isUnix()) {
                        sh 'pip install -r requirements.txt'
                    } else {
                        bat 'pip install -r requirements.txt'
                    }
                }
            }
        }

        // Stage 3: Execute tests
        stage('Run Selenium Tests') {
            steps {
                script {
                    // Running Selenium tests with pytest, capturing the output in JUnit XML and HTML report
                    if (isUnix()) {
                        sh 'pytest test_cases/test_keyword_driven.py --html=reports/report.html --junitxml=results.xml'
                    } else {
                        bat 'pytest test_cases/test_keyword_driven.py --html=reports/report.html --junitxml=results.xml'
                    }
                }
            }
        }

        // Stage 4: Archive results and reports
        stage('Archive Results') {
            steps {
                // Archive JUnit test results
                junit 'results.xml'
                
                // Archive the HTML report
                publishHTML (target: [
                    reportDir: 'reports',    // Folder where reports are stored
                    reportFiles: 'report.html',   // Name of the HTML file
                    reportName: 'Selenium Test Report'
                ])
            }
        }
    }

    // Post-build actions (optional)
    post {
        always {
            // Always clean up workspace after build
            cleanWs()

            // If something went wrong, this will display a console message
            failure {
                echo 'The build failed!'
            }
        }
    }
}
