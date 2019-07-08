#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main(void)
{
    char str[100];

    // file descriptors to listen from and communincate to
    int listen_fd, comm_fd;

    // struct that holds IP address and port numbers
    struct sockaddr_in servaddr;

    // initiate the listening socket to use IP addressing
    listen_fd = socket(AF_INET, SOCK_STREAM, 0);

    // clear the servaddr struct
    memset(&servaddr, 0, sizeof(servaddr));

    // set the values on the servaddr struct
    // set the addressing scheme to be IP addressing
    servaddr.sin_family = AF_INET;
    // allow any IP address to connect to this address
    servaddr.sin_addr.s_addr = htons(INADDR_ANY);
    // listen on port 8080
    servaddr.sin_port = htons(8080);

    // applying the settings we initialized on the servaddr on our socket
    bind(listen_fd, (struct sockaddr *)&servaddr, sizeof(servaddr));

    // start listening for connections
    // we'll only keep at most 10 connection requests alive
    // any connections after 10 will be dropped
    listen(listen_fd, 10);

    // init the write socket to accept a connection from any device
    // that wishes to connect
    // if no one wishes to connection, we'll just wait
    // this the socket that we'll be reading from and writing to
    // requests will come through here and
    // any data we want to send to the client gets written here
    comm_fd = accept(listen_fd, (struct sockaddr *)NULL, NULL);

    while (1)
    {
        // clear the str buffer
        memset(str, 0, 100);

        // read the first the 100 bytes from the socket
        read(comm_fd, str, 100);

        // print whatever was read from the socket
        printf("Echoing back - %s\n", str);

        // sending back the contents of str back to the client
        write(comm_fd, str, strlen(str) + 1);
    }

    return 0;
}
