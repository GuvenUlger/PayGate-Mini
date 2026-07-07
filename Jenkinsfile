pipeline {
    agent any

    stages {
        stage('1. Kodu GitHub\'dan Çek') {
            steps {
                echo 'GitHub\'dan en güncel kodlar çekiliyor...'
                git branch: 'main', url: 'https://github.com/GuvenUlger/PayGate-Mini.git'
            }
        }

        stage('2. Docker Imajını Derle') {
            steps {
                echo 'Uygulama ve testleri içeren Docker imajı basılıyor...'
                sh 'docker build -t paygate-mini:latest .'
            }
        }

        stage('3. Testleri Docker İçinde Koştur') {
            steps {
                echo 'Ödeme motoru kuralları izole Docker konteyneri içinde test ediliyor...'
                sh 'docker run --rm paygate-mini:latest python -m pytest test_app.py'
            }
        }

        stage('4. Canlı Ortama Dağıt (Deploy)') {
            steps {
                echo 'Eski çalışan konteyner temizleniyor...'
                sh 'docker stop paygate-container || true'
                sh 'docker rm paygate-container || true'
                sh 'docker run -d -p 8080:8080 --name paygate-container paygate-mini:latest'
            }
        }
    }

    post {
        success {
            echo 'CI/CD hattı başarıyla tamamlandı. Ödeme sistemi yayında!'
        }
        failure {
            echo '❌ Bir şeyler ters gitti!'
        }
    }
}