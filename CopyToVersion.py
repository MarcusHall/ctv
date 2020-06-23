#class CopyToVersion:

from pathlib import Path
import shutil
import argparse
import ConvertToBase36
import datetime

x = datetime.datetime.now()

print(x)

ds = x.strftime('%Y-%m-%d-%H-%M-%S')

print(ds)

#x = datetime.datetime(2070, 12, 13, 1, 48, 35)
#x = datetime.datetime(2085, 12, 13, 1, 48, 35)
#x = datetime.datetime(2087, 12, 13, 1, 48, 35)
#x = datetime.datetime(2999, 12, 13, 1, 48, 35)
x = datetime.datetime(3000, 12, 31, 23, 59, 59)

print(x)

x = int((x.timestamp() - datetime.datetime.now().timestamp())//1)

print(x)

y = ConvertToBase36.ConvertToBase36()

#j = y.ConvertToBase(x).rjust(5,'!')
k = y.ConvertToBase(x)
j = k.rjust(7,'!')

#print(string.rjust(width, fillchar))
print(k)
print(k[-9:])
print(k.rjust(7,'!'))
print(j)
print(j[-9:])
print(j.rjust(7,'!'))

parser = argparse.ArgumentParser()
parser.add_argument("file_path", help="first argument is file: to copy file to an archive reverse date time named file")
parser.add_argument("--test",help="testing mode makes no changes or deletions",action="store_true")
args = parser.parse_args()
print(args)
#   
# "C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\python.exe" "C:\Users\Administrator\Desktop\PythonScripts\CopyToVersion\ctv\CopyToVersion.py" "C:\temp\CTV test.txt"  > c:\temp\temp.txt
# "C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\python.exe" "C:\Users\Administrator\Desktop\PythonScripts\CopyToVersion\ctv\CopyToVersion.py" "C:\temp\CTV test.txt"
# Split filename into componenets
#        File directoryInfo = new File(CTV.fromFileName);
fromFile = Path(args.file_path)


#        // parse filename into pieces for splicing date stamp 
#        String fromFolder = directoryInfo.getParent();
#
#        String fromBaseFileName = directoryInfo.getName();
#        Integer indexOfFromExtFileName = fromBaseFileName.lastIndexOf(".");
#        String fromExtFileName = " ";
#
#        if (indexOfFromExtFileName != 0)
#        {
#            fromExtFileName = fromBaseFileName.substring(indexOfFromExtFileName);
#            fromBaseFileName = fromBaseFileName.substring(0, indexOfFromExtFileName);
#        }
#
# Rejoin with reverse date time for new name.
#toFile = Path(fromFile.parent + '/' + fromFile.stem + UTIL.DefaultReverseDateTime() + '.' + fromFile.suffix)
#toFile = Path(fromFile.parent + '/' + fromFile.stem + 'DefaultReverseDateTime' + '.' + fromFile.suffix)
#print(fromFile.parent )
#print(fromFile.stem)
#print('DefaultReverseDateTime')
#print('.')
#print(fromFile.suffix)
#print('/' + fromFile.stem)
toFile = Path(fromFile.parent).joinpath(fromFile.stem + '[' + j + ']' + ds + fromFile.suffix)
print(toFile.absolute())

       
# Copy file to new name
shutil.copy2(fromFile.absolute(),toFile.absolute())

# test filename for errors
#        File fromFile = new File(fromFileName);
#        File toFile = new File(toFileName);#
#
#        if (!fromFile.exists())
#            throw new IOException("FileCopy:" + "nosuchsourcefile:" + fromFileName);
#
#        if (!fromFile.isFile())
#            throw new IOException("FileCopy:" + "can't copy directory:" + fromFileName);
#
#        if (!fromFile.canRead())
#            throw new IOException("FileCopy:" + "sourcefileisunreadable:" + fromFileName);
#
#        if (toFile.isDirectory())
#            toFile = new File(toFile, fromFile.getName());
#
#        if (toFile.exists())
#        {
#            if (!toFile.canWrite())
#                throw new IOException("FileCopy:" + "destinationfileisunwriteable:" + toFileName);
#            System.out.print("Overwrite existing file" + toFile.getName() + "?(Y/N):");
#            System.out.flush();
#            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
#            String response = in.readLine();
#
#            if (!response.equals("Y") && !response.equals("y"))
#                throw new IOException("FileCopy:" + "existingfilewasnotoverwritten.");
#        }
#
#        else
#        {
#            String parent = toFile.getParent();#
#
#            if (parent == null)
#                parent = System.getProperty("user.dir");
#            File dir = new File(parent);
#
#            if (!dir.exists())
#3                throw new IOException("FileCopy:" + "destinationdirectorydoesn'texist:" + parent);
#
#            if (dir.isFile())
#                throw new IOException("FileCopy:" + "destinationisnotadirectory:" + parent);
#
#            if (!dir.canWrite())
#                throw new IOException("FileCopy:" + "destinationdirectoryisunwriteable:" + parent);
#        }
#


#package net.marcushall.ctv;
#
#import java.io.BufferedReader;
#import java.io.File;
#import java.io.FileInputStream;
#import java.io.FileOutputStream;
#import java.io.IOException;
#import java.io.InputStreamReader;

#import net.marcushall.util.*;


#public class CopyToVersion
#{
#    private String fromFileName;
#    private String toFileName;
#    //	private Integer maxNumberOfSeconds = 2238976115 916132831;
#
#
#    public static void main(String [] args)
#    {
#        CopyToVersion CTV = new CopyToVersion();
#        /*------------------------------------------------------------------------------------*/
#        /*  Get the args object */
#        /*------------------------------------------------------------------------------------*/
#        if (args.length == 0)
#        {
#        }
#        else
#        {
#            for (int i = 0; i < args.length; i++)
#            {
#                //			System.out.println(args[i].substring(1, 2)) ;
#                if (args[i].startsWith("/"))
#                {
#                    //					System.out.println(args[i].substring(1,2) + "}}}}");
#                    if (args[i].substring(1, 2).startsWith("r"))
#                    {
#                    //						System.out.println(reverseSort) ;
#                    }
#                    else
#                    {
#                    }
#                }
#                else
#                {
#                    CTV.fromFileName = args[i];
#                //					System.out.println(CTV.fromFileName) ;
#                }
#            }
#        }
#
#        DateFormats UTIL = new DateFormats() ;
#        // Maximum Value UTIL.clsTestCalendar.set(2070, Calendar.DECEMBER, 13, 1, 48, 35);
#        //		UTIL.clsTestCalendar.clear(Calendar.MILLISECOND);
#        // UTIL.defaultDateTime = UTIL.DefaultDateTime();
#
#        File directoryInfo = new File(CTV.fromFileName);
#
#        // parse filename into pieces for splicing date stamp 
#        String fromFolder = directoryInfo.getParent();
#
#       String fromBaseFileName = directoryInfo.getName();
#       Integer indexOfFromExtFileName = fromBaseFileName.lastIndexOf(".");
#       String fromExtFileName = " ";

#       if (indexOfFromExtFileName != 0)
#       {
#           fromExtFileName = fromBaseFileName.substring(indexOfFromExtFileName);
#           fromBaseFileName = fromBaseFileName.substring(0, indexOfFromExtFileName);
#       }
#       // Rejoin for new name.
#       CTV.toFileName = fromFolder + "\\" + fromBaseFileName + UTIL.DefaultReverseDateTime() + fromExtFileName;
#       
#       // Maximum Value CTV.clsTestCalendar.set(2070, Calendar.DECEMBER, 13, 1, 48, 35);
#       //		CTV.clsTestCalendar.clear(Calendar.MILLISECOND);

#       try
#       {
#           copy(CTV.fromFileName, CTV.toFileName);
#        //for (int i = 0; i < 36; i++)
#        //{
#        //	CTV.NewNameI(i);
#        //    copy(CTV.fromFileName,CTV.toFileName ) ;
#        //}
#       }
#       catch (IOException e)
#       {
#           System.err.println(e.getMessage());
#       }
#   }   // public static void Main(String[] args)

#   static void copy(String fromFileName, String toFileName) throws IOException
#   {
#       File fromFile = new File(fromFileName);
#       File toFile = new File(toFileName);

#       if (!fromFile.exists())
#           throw new IOException("FileCopy:" + "nosuchsourcefile:" + fromFileName);

#       if (!fromFile.isFile())
#           throw new IOException("FileCopy:" + "can't copy directory:" + fromFileName);

#       if (!fromFile.canRead())
#           throw new IOException("FileCopy:" + "sourcefileisunreadable:" + fromFileName);

#       if (toFile.isDirectory())
#           toFile = new File(toFile, fromFile.getName());

#       if (toFile.exists())
#       {
#           if (!toFile.canWrite())
#               throw new IOException("FileCopy:" + "destinationfileisunwriteable:" + toFileName);
#           System.out.print("Overwrite existing file" + toFile.getName() + "?(Y/N):");
#           System.out.flush();
#           BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
#           String response = in.readLine();

#           if (!response.equals("Y") && !response.equals("y"))
#               throw new IOException("FileCopy:" + "existingfilewasnotoverwritten.");
#       }

#       else
#       {
#           String parent = toFile.getParent();

#           if (parent == null)
#               parent = System.getProperty("user.dir");
#           File dir = new File(parent);

#           if (!dir.exists())
#               throw new IOException("FileCopy:" + "destinationdirectorydoesn'texist:" + parent);

#           if (dir.isFile())
#               throw new IOException("FileCopy:" + "destinationisnotadirectory:" + parent);

#           if (!dir.canWrite())
#               throw new IOException("FileCopy:" + "destinationdirectoryisunwriteable:" + parent);
#       }

#       FileInputStream from = null;
#       FileOutputStream to = null;

#       try
#       {
#           from = new FileInputStream(fromFile);
#           to = new FileOutputStream(toFile);
#           byte [] buffer = new byte[4096];
#           int bytesRead;

#           while ((bytesRead = from.read(buffer)) != -1)
#           {
#               to.write(buffer, 0, bytesRead);
#           }
#       }
#       finally
#       {
#           if (from != null)
#               try
#               {
#                   from.close();
#               }
#               catch (IOException e)
#               {
#                   ;
#               }

#           if (to != null)
#               try
#               {
#                   to.close();
#               }
#               catch (IOException e)
#               {
#                   ;
#               }
#       }
#   }   // public static void copy
#}   // class ctv
