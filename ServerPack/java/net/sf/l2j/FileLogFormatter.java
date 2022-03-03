package net.sf.l2j;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.logging.Formatter;
import java.util.logging.LogRecord;

import javolution.text.TextBuilder;

public class FileLogFormatter extends Formatter
{
	private static final String CRLF = "\r\n";
	private static final String SPACE = "\t";
	private SimpleDateFormat dateFmt = new SimpleDateFormat("yyyy.MM.dd HH:mm:ss,SSS");
	
	public String format(LogRecord record)
	{
        TextBuilder output = new TextBuilder();
		
		return output
		.append(dateFmt.format(new Date(record.getMillis())))
		.append(SPACE)
		.append(record.getLevel().getName())
		.append(SPACE)
		.append(record.getThreadID())
		.append(SPACE)
		.append(record.getLoggerName())
		.append(SPACE)
		.append(record.getMessage())
		.append(CRLF)
		.toString();
	}
}
