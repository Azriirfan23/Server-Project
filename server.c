#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <unistd.h>
#include <string.h>

int main(){

	char server_message[300] = "you havce reached the server\n";
	/*Create the server socket*/
	int server_socket, new_socket,c;
	struct sockaddr_in server_address, client;
	server_socket=socket(AF_INET, SOCK_STREAM,0);
	if(server_socket == -1)
	{
	printf("Could not create socket");
	}
	printf("Socket have been Created\n");
	/*define the server address*/

	server_address.sin_family = AF_INET;
	server_address.sin_port = htons(8888);
	server_address.sin_addr.s_addr = INADDR_ANY;

	//tO BIND THE SOCKET TO PRECIFIC IP AND PORT//
	if(bind(server_socket,(struct sockaddr*) & server_address , sizeof(server_address))<0)
	{
	puts("Bind Failed");
	}
	puts("Bind Done");
	//Listen//

	listen(server_socket, 3);

	//Accepct incoming calls //

	puts("Waiting for connection");
	c = sizeof(struct sockaddr_in);
	while((new_socket = accept(server_socket, (struct sockaddr *)&client, (socklen_t*)&c)))
	{
		puts("Connection accepted");
		//Reply to the client
		char message[300]= "IP Address for www.google.com is 142.250.199.36 ";
		//message = "Hello Client , I have received your connection. But I have to go now, bye\n";
		write(new_socket , message , strlen(message));

	}
	if (new_socket<0)
	{
		perror("accept failed");
	}

	puts("Connection accepted");

	int client_socket;
	client_socket = accept(server_socket,NULL,NULL);

	//send the message//
	send(client_socket,server_message,sizeof(server_message),0);

	//close the socket//
	close(server_socket);

	return 0;
}

