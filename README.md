FOUND THE PROBLEM!
Tic-Tac-Toe Web App - Complete Deployment SOP
Repository: https://github.com/yourusername/tic-tac-toe

📁 Repository Structure
text
tic-tac-toe/
├── app.py                 # Flask backend
├── requirements.txt       # Flask==3.0.3
├── Dockerfile            # Python 3.11 slim
├── templates/
│   └── index.html        # Tic-Tac-Toe UI
├── docker-compose.yml    # Production deployment
└── README.md             # This SOP
🚀 Quick Launch (EC2)
Prerequisites
AWS EC2 (Ubuntu 24.04 / Amazon Linux 2023, t2.micro+)

Security Group: TCP 5000 inbound

SSH key access

1. SSH & Setup
bash
ssh -i your-key.pem ubuntu@your-ec2-ip
sudo apt update && sudo apt install docker.io docker-compose git -y
sudo usermod -aG docker ubuntu && newgrp docker
2. Deploy (3 Commands)
bash
git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe
docker compose up -d --build
3. Verify
bash
docker ps                    # tictactoe: Up
docker compose logs -f       # Flask running on 0.0.0.0:5000
curl http://localhost:5000   # HTML response
🎮 Play: http://your-ec2-public-ip:5000

🐳 Docker Commands (Manual)
bash
# Build
docker build -t tictactoe .

# Run
docker run -d --name tictactoe -p 5000:5000 --restart unless-stopped tictactoe

# Logs/Status
docker logs -f tictactoe
docker ps

# Update (git pull)
git pull && docker compose up -d --build
🔧 Troubleshooting
Issue	Command	Expected
Container restarting	docker logs tictactoe	Running on 0.0.0.0:5000
Port conflict	sudo lsof -i :5000
docker run -p 8080:5000 ...	-
No Flask	cat requirements.txt
docker build --no-cache	Flask==3.0.3
404 templates	ls templates/	index.html
📝 docker-compose.yml (Full)
text
version: "3.9"
services:
  tictactoe:
    build: .
    container_name: tictactoe
    ports:
      - "5000:5000"
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000"]
      interval: 30s
      timeout: 10s
      retries: 3
🌐 Features
✅ 2-player browser Tic-Tac-Toe

✅ Auto-restart on crash

✅ Health checks

✅ Responsive UI

✅ New Game button

📱 Access Anywhere
text
Browser: http://your-ec2-public-ip:5000
Mobile: Same URL
Copy this README.md to your repo root. One-click deploy for anyone!