package cms;

my $netid = $ARGV[0];
my $homeworkhandle = $ARGV[1];

if (defined $homeworkhandle) {
    open (HOMEWORK, $homeworkhandle);
    open (SAVEDHW, ">", $netid.".zip");
    foreach (<HOMEWORK>){
        print SAVEDHW $_;
    }
    close(SAVEDHW);
    close(HOMEWORK);
    unlink $homeworkhandle;
}

if (open (NETID, $netid.".zip")){
    open(LOGFILE, '>>', "hw_log.txt") or die "Error opening log";
    print LOGFILE $netid;
    close (NETID);
    close (LOGFILE);
}

1;