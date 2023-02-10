#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int eleitor = 0; eleitor < voter_count; eleitor++)
    {

        // Query for each rank
        for (int preferencia = 0; preferencia < candidate_count; preferencia++)
        {
            string name = get_string("Rank %i: ", preferencia + 1);

            // Record vote, unless it's invalid
            if (vote(eleitor, preferencia, name) == false)
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    //se nome do candidato = nome do voto, esse eleitor no rank++ tem essa preferencia, repita pelo
    //numero de candidatos
    //se nao achar uma comparação, return false
    for (int x = 0; x < candidate_count; x++)
    {
        if (strcmp(name, candidates[x].name) == 0)
        {
           preferences[voter][rank] = x;
           return true;
        }
    }
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    for(int eleitor = 0; eleitor < voter_count; eleitor++)
    {
        for (int rank = 0; rank < candidate_count; rank++)
        {
             int c = preferences[eleitor][rank];
            if (candidates[c].eliminated == false)
            {
                candidates[c].votes++;
                break;
            }
        }
    }
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    //if algum candidate[x].votes > totalvotes/2, ele ganha e bool true ----> if bool true print candidate[x]
    //senão bool false e continua
    for (int x = 0; x < candidate_count; x++)
    {
    if (candidates[x].votes > (voter_count / 2))
    {
        printf("%s\n", candidates[x].name);
        return true;
    }
    }
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    //checa o numero de votos de todos os canditados com um for loop x, if candidate[x].votes = least votes
    int leastVotes = voter_count + 1;
    for (int x = 0; x < candidate_count; x++)
    {
        if (candidates[x].votes < leastVotes && candidates[x].eliminated == false)
        {
            leastVotes = candidates[x].votes;
        }
    }
    return leastVotes;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    //com o least_votes e checa se tem mais candidates com isso e isTie++
    //se isTie == numero de candidatos bool tie true
    //acaba com tudo e declara tie
    int isTie = 0;
    int stillRunning = 0;

    for (int x = 0; x < candidate_count; x++)
    {
        if (candidates[x].votes == min && candidates[x].eliminated == false)
        {
            stillRunning++;
            isTie++;
        }
        else if (candidates[x].eliminated == false)
        {
            stillRunning++;
        }
    }
    if (stillRunning == isTie)
    {
        return true;
    }
    return false;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    //com o lestvotes, depois de is_tie, elimina aqueles com candidates[x].votes = leastvotes
    //com bool eliminated = true
    for (int x = 0; x < candidate_count; x++)
    {
        if (candidates[x].eliminated == false && candidates[x].votes == min)
        {
            candidates[x].eliminated = true;
        }
    }

    return;
}
