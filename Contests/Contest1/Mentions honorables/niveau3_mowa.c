/**
 * @file main.c
 * @brief Discord contest - Jeu du plus ou moins.
 * @version 0.1
 * @date 2023-07-10
 * 
 * @copyright Copyright (c) 2023
 */

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/*************LOCALS*/
static void cheating_computer_ex3( void );

int main(){
    /* Start by printing a welcome banner */
    printf("Challenge Discord : Devos Code !\r\n\r\n");

    /* Initialize pseudo-random generator */
    srand( time( NULL ) );

    /* Challenge */
    cheating_computer_ex3();
    fflush(stdin);

    return 0;
}

/*************LOCALS*/
static void cheating_computer_ex3( void ){
    bool player_won = false;
    unsigned short game_turn = 1;
    unsigned short player_guess = 0;
    unsigned short min_guess = 0;
    unsigned short max_guess = 100;

    printf("CHALL3: Le nombre caché a été aléatoirement choisi.. ;)\r\n");

    do{
        /* Get player guess */
        printf("Proposition n°%d: ", game_turn);
        if( scanf("%hu", &player_guess) == 0 ){
            fflush(stdin);
            continue;
        }

        /* Sanitize player guess (can't be less than 0 and greater than 100) */
        if( player_guess < 0 || player_guess > 100 ){
            printf("Votre proposition doit être comprise entre 0 et 100.\r\n\r\n");
            continue;
        }

        /* Sanitize player guess (can't be less to min_guess and greater to max_guess) */
        if( player_guess <= min_guess || player_guess >= max_guess ){
            printf("Votre proposition n'est pas cohérente avec les réponses précédentes.\r\n\r\n");
            continue;
        }

        /* Player guess is valid, try to fool the player */
        unsigned short delta_with_max = max_guess - player_guess;
        unsigned short delta_with_min = player_guess - min_guess;

        /* If delta_with_max is greater than delta_with_min, it means that the 
            player guess is closer to the min_guess */
        if( delta_with_max > delta_with_min ){
            min_guess = player_guess;

            printf("Plus grand\r\n\r\n");
            game_turn++;
        }
        /* If delta_with_max is lower than delta_with_min, it means that the 
            player guess is closer to the max_guess */
        else if( delta_with_max < delta_with_min ){
            max_guess = player_guess;

            printf("Plus petit\r\n\r\n");
            game_turn++;
        }
        /* 
         * If delta_with_max equals delta_with_min, by default, indicate that the hidden number is lower
         * If delta between min and max equals 1, player can't be fooled anymore, as he discovered the min and max.
         */
        else{
            max_guess = player_guess;

            if( max_guess - min_guess <= 1 ){
                printf("Gagné\r\n\r\n");
                player_won = true;
            }
            else{
                printf("Plus petit\r\n\r\n");
                game_turn++;
            }
        }
    }while( player_won != true );

    printf("Nombre %d trouvé en %d tours !\r\n\r\n", player_guess, game_turn);
}