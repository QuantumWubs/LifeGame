# TODO: Make P2P connection with Transaction Partner
    # Create Node
    # Get Location of Partner Node
    # Connect to Partner Node
        #Make Check to make sure Shared Key is the same (Cipher)

    # Specify who is the Recipient
# TODO: (IF this Client is Payer): Get Specified amount (To Transact)
ACTION = input('>').upper()
if(ACTION == 'T'):
    print('========[ Transact ]========')
    while(ACTION == 'T'):
        Partner = input('\nInput Partner ID\n>')
        TransAction = input('\nAction Send(S)/Receive(R)/Cancel(X)\n>').upper()

        while(TransAction == 'S'):
            # TODO: Send Token
            print('Send Code')

        while(TransAction == 'R'):
            # TODO: Receive Token
            print('Receive Code')

        if(TransAction == 'X'):
            if(input('Are you sure? (Y/N)').upper() == 'Y'):
                break
