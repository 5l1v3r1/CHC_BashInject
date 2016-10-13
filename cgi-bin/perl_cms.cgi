#!/usr/bin/perl
#File: perl_cms.cgi
use CGI;
use strict;

#what would happen if we didn't have this? ;)
$ENV{'PATH'} = '/bin:/usr/bin:/usr/local/bin';

use CGI;
my $q = CGI->new;
print header

$cmshtml = "../templates/perl_cms.html"
$homehtml = "../"
$content = "";

if (defined ($q->upload('homework'))) {
	if (open (<HOMEWORK>, $q->upload('homework'))){

		#write netid to logfile: hw_log.txt
		if (open (<NETID>, $q->param('netid'))){
			open(LOGFILE, '>>', "hw_log.txt")
			print <NETID>
			close (NETID)
			close (LOGFILE)
		}
		while(){
			$content.=$_;
		}
		close(HOMEWORK);
	}
	$print $content; #
} else { #assume we just loaded page
	FRONTHTML();
	BACKHTML();
}

exit 0;
#RFI/LFI vulnerability in GET request for a file


sub FRONTHTML {
print << EOF;
Content-Type: text/html
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Perl CMS | Cornell Hacking Club</title>

    <!-- Bootstrap Core CSS -->
    <link href="../../static/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="../../static/css/modern-business.css" rel="stylesheet">
    <link href="../../static/css/general.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="../../static/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
</head>

<body>


<!-- Page Content -->
<div class="container">

    <!-- Page Heading/Breadcrumbs -->
    <div class="row">
        <div class="col-lg-12 ">
            <h1 class="page-header">Welcome to Perl CMS</h1>
            <ol class="breadcrumb">
                <li><a href="../">Home</a>
                </li>
                <li class="active">Perl CMS!</li>
            </ol>
        </div>
    </div>
    <!-- /.row -->

    <div class="container">
        <div class="row">
            <div class="col-sm-6 col-md-4 col-md-offset-4">
                <div>	
EOF
}


sub BACKHTML {
print << EOF;
               </div>

            </div>
        </div>
    </div>



    <hr>
 

    <!-- Footer -->
    <footer>
        <div class="row">
            <div class="col-lg-12">
                <p>Copyright &copy; Cornell Hacking Club 2016</p>
            </div>
        </div>
    </footer>

</div>
<!-- /.container -->

 </body>

</html>
EOF
}

#forms
print header();
print start_html(	
  -title=>'Perl CMS!',
	)
print h1('Welcome to Perl CMS')
print start_form('POST', 'perl_cms.cgi' ,&CGI::MULTIPART);
print textfield('netid', 'netid', 50, 80);
print filefield('homework');
print submit('submit_hw');
print hidden('cmd','cat'); #code injection
print end_form;
print end_html

