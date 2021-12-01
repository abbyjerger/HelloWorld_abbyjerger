/*
A KBase module: HelloWorld_abbyjerger
*/

module HelloWorld_abbyjerger {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_HelloWorld_abbyjerger(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
