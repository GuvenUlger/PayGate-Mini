pipeline {
    agent any

    stages {
        stage('1. Kodu GitHub\'dan Çek') {
            steps {
                echo 'Kodlar indiriliyor...'
                checkout scm
            }
        }

        stage('2. Docker Imajını Derle') {
            steps {
                echo 'Uygulama ve testleri içeren Docker imajı basılıyor...'
                // sh yerine 'bat' kullanarak Windows komut satırını doğrudan tetikliyoruz
                bat 'docker build -t paygate-mini:latest .'
            }
        }

        stage('3. Testleri Docker İçinde Koştur') {
            steps {
                echo 'Ödeme motoru kuralları izole Docker konteyneri içinde test ediliyor...'
                bat 'docker run --rm paygate-mini:latest python -m pytest test_app.py'
            }
        }

        stage('4. Canlı Ortama Dağıt (Deploy)') {
            steps {
                echo 'Eski çalışan konteyner temizleniyor ve yenisi ayağa kaldırılıyor...'
                bat 'docker stop paygate-container || true'
                bat 'docker rm paygate-container || true'
                bat 'docker run -d -p 8080:8080 --name paygate-container paygate-mini:latest'
            }
        }
    }

    post {
        success {
            echo '🎉 Tebrikler Güven! CI/CD hattı başarıyla tamamlandı. Ödeme sistemi yayında!'
        }
        failure {
            echo '❌ Bir şeyler ters gitti! Logları incele.'
        }
    }
}