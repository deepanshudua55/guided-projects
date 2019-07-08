#include <stdio.h>
#include <string.h>

/*  
T / HTTP/1.1
Host: www.example.com
Connection: close
X-Header: whatever
*/

int main(void)
{

    // parsing our request
    char *request = "GET /foobar HTTP/1.1\nHost: www.example.com\nConnection: close\nX-Header: whatever\n\n";

    char method[200];
    char path[8192];
    char http[8192];

    sscanf(request, "%s %s", method, path);

    printf("method: %s\n", method);
    printf("path: %s\n", path);

    // build our response
    char response[500000];

    char *body = "<h1>Hello World!</h1>";
    int content_length = strlen(body);

    sprintf(response, "HTTP/1.1 200 OK\n"
                      "Content-Type: text/html\n"
                      "Content-Length: %d\n"
                      "Connection: close\n"
                      "\n"
                      "%s",
            content_length, body);

    printf("%s", response);

    return 0;
}