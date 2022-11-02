assigment 1:

(1)先建立socket連到mailserversmtp.mailtrap.io
(2)send EHLO command
(3)send AUTHcommand
(4)send MAIL FROM command
(5)send RCPT TO command
(6)send DATA command 
(7)send message data(輸入recipient’s email address和message context)
(8)Send QUIT command


assigment 2 :

(1)在終端機中檔案目錄下輸入python Iperfer.py -s -p <listen port>即可開始運行server，<listen port>可自行決定，但須在1024到65535之間
(2)再開一個終端機視窗，在檔案目錄下輸入python Iperfer.py -c -h <IP address> -p <listen port> -t <time>，<time>以秒為單位，必須為正整數
(3) 即可得client送出的資料數和傳送率(Mbps)，以及server接收的資料數和接收率(Mbps)，若輸入資訊有誤(例如少參數，或多參數)則會顯示error
	
	     