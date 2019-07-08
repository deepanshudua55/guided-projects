#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main(void)
{
    int sockfd;

    // a buffer to hold the data we'll be sending
    char sendline[100];
    // a buffer to hold the data we'll be receiving from the server
    char recvline[100];
    // struct that holds info such as IP address and port numbers
    struct sockaddr_in servaddr;

    // init the socket to use IP addressing
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    // clear the servaddr struct (this is a formality that needs to happen)
    bzero(&servaddr, sizeof(servaddr));

    // Setting values on the servaddr struct:
    // set addressing scheme to IP addressing
    servaddr.sin_family = AF_INET;
    // listen on port 8080
    servaddr.sin_port = htons(8080);

    // set the IP address of servaddr to '127.0.0.1'
    // the address in servaddr needs to be in int format
    // hence the usage of inet_pton
    inet_pton(AF_INET, "127.0.0.1", &(servaddr.sin_addr));

    // connect to the device with the given address and port no in servaddr
    connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr));

    while (1)
    {
        // clear the sendline buffer
        memset(sendline, 0, 100);
        // clear the recvline buffer
        memset(recvline, 0, 100);
        // read at most 100 bytes from stdin into the sendline buffer
        fgets(sendline, 100, stdin);

        // write the contents of the sendline buffer to the socket
        write(sockfd, sendline, strlen(sendline) + 1);
        // read at most 100 bytes from the socket into the recvline buffer
        read(sockfd, recvline, 100);
        // print the contents of the recvline buffer
        printf("%s", recvline);
    }

    return 0;
}