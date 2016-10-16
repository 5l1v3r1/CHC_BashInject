#!/usr/bin/perl
#File: perl_cms.cgi
use CGI;

$ENV{'PATH'} = '/bin:/usr/bin:/usr/local/bin';

$cgi = new CGI;
FRONTHTML();
FORMHTML();

if ($cgi->param){

	#save homework to hwfiles path
	$hwpath =  "../hwfiles/";
	$hwhandle = $cgi->upload('homework');
	if (defined $hwhandle) {
		print $cgi->header(-type=>"text/plain");
		open (HOMEWORK, $CGI->param('homework'));
		open (SAVEDHW, ">", $hwpath.$cgi->param('homework'));
		print <SAVEDHW> <HOMEWORK>; #save the contents of homework
		close(SAVEDHW);
		close (HOMEWORK);
	}

	#save netid to guestbook
	#consider changiing hw_log.txt to hidden script
	if (open (NETID, $cgi->param('netid'))){
		open(LOGFILE, '>>', "hw_log.txt");
		print <LOGFILE> <NETID>;
		close (NETID);
		close (LOGFILE);
	}

}

BACKHTML();

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

sub FORMHTML {
print << EOF;
	<h3>Upload Homework Here!</h3>  <!---Add a URL for here.-->
    <FORM class="form-signin" METHOD="POST" action="{% url 'perl_cms'%}" enctype="multipart/form-data">
    <input type="text" class="form-control" name="netid" placeholder="netid" required autofocus>
    <label for="homework">Upload Homework</label>
    <input type="file" class="form-control" name="homework" >
    <input type="hidden"  name="lastlocation" value="perl_cms">
    <button class="btn btn-lg btn-primary btn-block" type="submit">
        Upload
    </button>
	</FORM>
EOF
}
#alt script 
# print header();
# print start_html(	
#   -title=>'Perl CMS!',
# 	)
# print h1('Welcome to Perl CMS')
# print start_form('POST', 'perl_cms.cgi' ,&CGI::MULTIPART);
# print textfield('netid', 'netid', 50, 80);
# print filefield('homework');
# print submit('submit_hw');
# print hidden('cmd','cat'); #code injection
# print end_form;


