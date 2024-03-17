// #include<stdio.h>

// int length(int arr[],int len)
// {
//     return len;
// }

// void ascending(int arr[],int arr2[],int length)
// {
    
// }



// int main()
// {
//     int numbers[] = {1,2,3,4,5};
//     int len = length(numbers,sizeof(numbers)/sizeof(numbers[0]));
//     printf("%d",len);
    
// }




#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to compare strings for ascending order
int compareAsc(const void *a, const void *b) {
    return strcmp(*(const char **)a, *(const char **)b);
}

// Function to compare strings for descending order
int compareDesc(const void *a, const void *b) {
    return strcmp(*(const char **)b, *(const char **)a);
}

int main() {
    int n;

    // Input the number of strings
    printf("Enter the number of strings: ");
    scanf("%d", &n);

    // Input the strings
    char **arr = (char **)malloc(n * sizeof(char *));
    printf("Enter %d strings:\n", n);
    for (int i = 0; i < n; i++) {
        arr[i] = (char *)malloc(100 * sizeof(char)); // Assuming a maximum string length of 100
        scanf("%s", arr[i]);
    }

    // Sorting in ascending order
    qsort(arr, n, sizeof(char *), compareAsc);

    // Displaying sorted array in ascending order
    printf("\nSorted in ascending order:\n");
    for (int i = 0; i < n; i++) {
        printf("%s\n", arr[i]);
    }

    // Sorting in descending order
    qsort(arr, n, sizeof(char *), compareDesc);

    // Displaying sorted array in descending order
    printf("\nSorted in descending order:\n");
    for (int i = 0; i < n; i++) {
        printf("%s\n", arr[i]);
    }

    // Free allocated memory
    for (int i = 0; i < n; i++) {
        free(arr[i]);
    }
    free(arr);

    return 0;
}
