pipeline {
    agent any
    stages {
        stage('1.Kodu GitHub\'dan Çek'){
            steps {
                echo 'GitHub\'daki en güncel kodlar Jenkins çalışma alanına indiriliyor...'
                checkout scm
            }
        }

        stage('2. Otomatik Testleri Çalıştır (PyTest)') {
            steps {
                echo 'Ödeme motorunun kuralları test ediliyor...'
                sh 'python -m pytest test_app.py'
            }
        }

        stage('3. Docker Imajını Yeniden Derle') {
            steps {
                echo 'Testler başarıyla geçti! Yeni Docker imajı başlıyor...'
                sh 'docker build -t paygate-mini:latest .'
            }
        }

        stage('4. Canlı Ortama Dağıt (Depoloy)') {
            steps {
                echo 'Eski çalışan konteyner varsa durduruluyor ve yenisi ayağa kaldırılıyor...'
                sh 'docker stop paygate-container || true'
                sh 'docker rm paygate-container || true'
                sh 'docker run -d -p 8080:8080 --name paygate-container paygate-mini:latest'
            }
        }
    }

    post {
        success {
            echo 'Tebrikler CI/CD hattı başarıyla tamamlandı! Ödeme sistemi yayında.'
        }
        failure {
            echo 'Hata oluştu! Lütfen logları kontrol edin ve hatayı düzeltin.'
        }
    }
}