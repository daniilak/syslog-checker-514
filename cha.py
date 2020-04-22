import syslog
syslog.openlog(ident="LOG_IDENTIFIER",logoption=syslog.LOG_PID, facility=syslog.LOG_LOCAL0)
syslog.syslog('Log processing initiated...')
