id0
Code snippet:
```
LambdaForm customize(MethodHandle mh){
  LambdaForm customForm=new LambdaForm(debugName,arity,names,result,forceInline,mh);
  if (COMPILE_THRESHOLD > 0 && isCompiled) {
    customForm.compileToBytecode();
  }
  customForm.transformCache=this;
  return customForm;
}
```
Original comment:
```
Customize LambdaForm for a particular MethodHandle
```
Generated comment:
```
Create a method invocation.
```
---
id1
Code snippet:
```
public IndirectionException(int offset){
  super(\"\",0,org.omg.CORBA.CompletionStatus.COMPLETED_MAYBE);
  this.offset=offset;
}
```
Original comment:
```
Creates an IndirectionException with the right offset value. The stream offset is returned in the exception\'s offset field. This exception is constructed and thrown during reading recursively defined values off of a stream.
```
Generated comment:
```
Constructs a new exception with the specified detail message. the cause is not initialized.
```
---
id2
Code snippet:
```
public static ValueExp times(ValueExp value1,ValueExp value2){
  return new BinaryOpValueExp(TIMES,value1,value2);
}
```
Original comment:
```
Returns a binary expression representing the product of two numeric values.
```
Generated comment:
```
Returns a new instance with the specified value.
```
---
id3
Code snippet:
```
public TableRowSorter(){
  this(null);
}
```
Original comment:
```
Creates a <code>TableRowSorter</code> with an empty model.
```
Generated comment:
```
Constructs a new <code>sortedsetsorter</code> instance.
```
---
id4
Code snippet:
```
public void namespaceAfterStartElement(String uri,String prefix) throws SAXException {
}
```
Original comment:
```
This method is used when a prefix/uri namespace mapping is indicated after the element was started with a  startElement() and before and endElement(). startPrefixMapping(prefix,uri) would be used before the startElement() call.
```
Generated comment:
```
Receive notification of the end of an element.
```
---
id5
Code snippet:
```
private boolean isThisSiteID(String sourceID){
  return ((String)SAMLServiceManager.getAttribute(SAMLConstants.SITE_ID)).equals(sourceID) ? true : false;
}
```
Original comment:
```
Verifies if the sourceID passed in the parameter is same as this site\'s site ID.
```
Generated comment:
```
Returns true if the given method is a method.
```
---
id6
Code snippet:
```
@Override public int doStartTag() throws JspException {
  i=0;
  return EVAL_BODY_BUFFERED;
}
```
Original comment:
```
Process start tag
```
Generated comment:
```
Returns the start of the tag.
```
---
id7
Code snippet:
```
public void testRemoveAttributeNS() throws Throwable {
  Document doc;
  Element element;
  boolean state;
  Attr attribute;
  doc=(Document)load(\"staff\",builder);
  element=doc.createElementNS(\"http://www.w3.org/DOM\",\"elem\");
  attribute=doc.createAttributeNS(\"http://www.w3.org/DOM/Test/createAttributeNS\",\"attr\");
  element.setAttributeNodeNS(attribute);
  element.removeAttributeNS(\"http://www.w3.org/DOM/Test/createAttributeNS\",\"attr\");
  state=element.hasAttributeNS(\"http://www.w3.org/DOM/Test/createAttributeNS\",\"attr\");
  assertFalse(\"elementremoveattributens01\",state);
}
```
Original comment:
```
Runs the test case.
```
Generated comment:
```
Runs the test case.
```
---
id8
Code snippet:
```
boolean containsNamingContext(DN dn){
  return privateNamingContexts.containsKey(dn) || publicNamingContexts.containsKey(dn);
}
```
Original comment:
```
Indicates whether the specified DN is contained in this registry as a naming contexts.
```
Generated comment:
```
Returns true if the given id is contained in this context.
```
---
id9
Code snippet:
```
public int hashCode(){
  return getName().hashCode();
}
```
Original comment:
```
Returns the hash code value for this object.
```
Generated comment:
```
Returns a hash code for this instance.
```
---
id10
Code snippet:
```
@Override public void write(ASN1Writer stream) throws IOException {
  stream.writeStartSequence(OP_TYPE_INTERMEDIATE_RESPONSE);
  if (oid != null) {
    stream.writeOctetString(TYPE_INTERMEDIATE_RESPONSE_OID,oid);
  }
  if (value != null) {
    stream.writeOctetString(TYPE_INTERMEDIATE_RESPONSE_VALUE,value);
  }
  stream.writeEndSequence();
}
```
Original comment:
```
Writes this protocol op to an ASN.1 output stream.
```
Generated comment:
```
Encode the parameter list.
```
---
id11
Code snippet:
```
public String toString(){
  return \"[Digest Input Stream] \" + digest.toString();
}
```
Original comment:
```
Prints a string representation of this digest input stream and its associated message digest object.
```
Generated comment:
```
Returns a string representation of this object.
```
---
id12
Code snippet:
```
@Override public LocalDate dateYearDay(Era era,int yearOfEra,int dayOfYear){
  return dateYearDay(prolepticYear(era,yearOfEra),dayOfYear);
}
```
Original comment:
```
Obtains an ISO local date from the era, year-of-era and day-of-year fields.
```
Generated comment:
```
Returns a copy of this date with the day of year field updated. <p> localdatemidnight is immutable, so there are no set methods. instead, this method returns a new instance with the value of year changed.
```
---
id13
Code snippet:
```
public ContextRuleSet(){
  this(\"\");
}
```
Original comment:
```
Construct an instance of this <code>RuleSet</code> with the default matching pattern prefix.
```
Generated comment:
```
Creates a new instance.
```
---
id14
Code snippet:
```
private PageSize ensureDocumentHasNPages(int n,PageSize customPageSize){
  PageSize lastPageSize=null;
  while (document.getPdfDocument().getNumberOfPages() < n) {
    lastPageSize=addNewPage(customPageSize);
  }
  return lastPageSize;
}
```
Original comment:
```
Adds some pages so that the overall number is at least n. Returns the page size of the n\'th page.
```
Generated comment:
```
Ensures that the given document is not empty.
```
---
id15
Code snippet:
```
public static Mp4BoxHeader seekWithinLevel(ByteBuffer data,String id) throws IOException {
  logger.finer(\"Started searching for:\" + id + \" in bytebuffer at\"+ data.position());
  Mp4BoxHeader boxHeader=new Mp4BoxHeader();
  if (data.remaining() >= Mp4BoxHeader.HEADER_LENGTH) {
    boxHeader.update(data);
  }
 else {
    return null;
  }
  while (!boxHeader.getId().equals(id)) {
    logger.finer(\"Found:\" + boxHeader.getId() + \" Still searching for:\"+ id+ \" in bytebuffer at\"+ data.position());
    if (boxHeader.getLength() < Mp4BoxHeader.HEADER_LENGTH) {
      return null;
    }
    if (data.remaining() < (boxHeader.getLength() - HEADER_LENGTH)) {
      return null;
    }
    data.position(data.position() + (boxHeader.getLength() - HEADER_LENGTH));
    if (data.remaining() >= Mp4BoxHeader.HEADER_LENGTH) {
      boxHeader.update(data);
    }
 else {
      return null;
    }
  }
  logger.finer(\"Found:\" + id + \" in bytebuffer at\"+ data.position());
  return boxHeader;
}
```
Original comment:
```
Seek for box with the specified id starting from the current location of filepointer, Note it won\'t find the box if it is contained with a level below the current level, nor if we are at a parent atom that also contains data and we havent yet processed the data. It will work if we are at the start of a child box even if it not the required box as long as the box we are looking for is the same level (or the level above in some cases).
```
Generated comment:
```
Performs a bin search.
```
---
id16
Code snippet:
```
public void handleOpenError(File file,Throwable ex){
  System.err.println(ERR_LOGGER_ERROR_OPENING_FILE.get(file,publisherConfigDN,stackTraceToSingleLineString(ex)));
}
```
Original comment:
```
Handle an exception which occurred while trying to open a log file.
```
Generated comment:
```
This method is called when a line is encountered.
```
---
id17
Code snippet:
```
public void testConstructorSignBytesNegative7(){
  byte aBytes[]={-12,56,100,-2,-76,89,45,91,3,-15,23,-101};
  int aSign=-1;
  byte rBytes[]={-1,11,-57,-101,1,75,-90,-46,-92,-4,14,-24,101};
  BigInteger aNumber=new BigInteger(aSign,aBytes);
  byte resBytes[]=new byte[rBytes.length];
  resBytes=aNumber.toByteArray();
  for (int i=0; i < resBytes.length; i++) {
    assertTrue(resBytes[i] == rBytes[i]);
  }
  assertEquals(\"incorrect sign\",-1,aNumber.signum());
}
```
Original comment:
```
Create a negative number from a sign and an array of bytes. The number of bytes is multiple of 4. The most significant byte is negative.
```
Generated comment:
```
Create a negative number from a sign and an array of bytes. the number of bytes is 4.
```
---
id18
Code snippet:
```
public SubResourceCollection glueObjectClass(final String objectClass){
  this.glueObjectClasses.add(objectClass);
  return this;
}
```
Original comment:
```
Specifies an LDAP object class which is to be associated with any intermediate \"glue\" entries forming the DN template. Multiple object classes may be specified.
```
Generated comment:
```
Returns a new instance of the specified class.
```
---
id19
Code snippet:
```
public static MatchedValuesFilter createExtensibleMatchFilter(AttributeType attributeType,MatchingRule matchingRule,ByteString assertionValue){
  Reject.ifNull(attributeType,matchingRule,assertionValue);
  String rawAttributeType=attributeType.getNameOrOID();
  String matchingRuleID=matchingRule.getOID();
  MatchedValuesFilter filter=new MatchedValuesFilter(EXTENSIBLE_MATCH_TYPE,rawAttributeType,assertionValue,null,null,null,matchingRuleID);
  filter.attributeType=attributeType;
  filter.assertionValue=assertionValue;
  filter.matchingRule=matchingRule;
  return filter;
}
```
Original comment:
```
Creates a new extensibleMatch filter with the provided information.
```
Generated comment:
```
Creates a <code>filter</code> instance.
```
---
id20
Code snippet:
```
public boolean equals(Object o){
  if (o == null) {
    return false;
  }
  if (this == o) {
    return true;
  }
  if (!(o instanceof NTPrincipal)) {
    return false;
  }
  NTPrincipal that=(NTPrincipal)o;
  return this.getName().equals(that.getName());
}
```
Original comment:
```
Compares the specified Object with this <code>NTPrincipal</code> for equality.  Returns <code>true</code> if the given object is also a <code>NTPrincipal</code> and the two <code>NTPrincipal</code>s have the same user name.
```
Generated comment:
```
Tests this instance for equality with an arbitrary object.
```
---
id21
Code snippet:
```
public void callback(String instanceId,String callback,String data){
  callback(instanceId,callback,data,false);
}
```
Original comment:
```
Invoke JavaScript callback
```
Generated comment:
```
This method is called when the user presses the \"enter\" button.
```
---
id22
Code snippet:
```
protected void ensureMyLastProtocolMessagesHaveRecords(List<ProtocolMessage> protocolMessages){
  for (int pmPointer=0; pmPointer < protocolMessages.size(); pmPointer++) {
    ProtocolMessage pm=protocolMessages.get(pmPointer);
    if (handlingMyLastProtocolMessageWithContentType(protocolMessages,pmPointer)) {
      if (pm.getRecords() == null || pm.getRecords().isEmpty()) {
        pm.addRecord(new Record());
      }
    }
  }
}
```
Original comment:
```
Every last protocol message that is going to be sent from my peer has to have a record.
```
Generated comment:
```
Ensures that the message is not null.
```
---
id23
Code snippet:
```
public static float signum(float f){
  return (f == 0.0f || Float.isNaN(f)) ? f : copySign(1.0f,f);
}
```
Original comment:
```
Returns the signum function of the argument; zero if the argument is zero, 1.0f if the argument is greater than zero, -1.0f if the argument is less than zero. <p>Special Cases: <ul> <li> If the argument is NaN, then the result is NaN. <li> If the argument is positive zero or negative zero, then the result is the same as the argument. </ul>
```
Generated comment:
```
Returns the sign of the argument.
```
---
id24
Code snippet:
```
public AnnotationVisitor visitTypeAnnotation(int typeRef,TypePath typePath,String desc,boolean visible){
  if (api < Opcodes.ASM5) {
    throw new RuntimeException();
  }
  if (cv != null) {
    return cv.visitTypeAnnotation(typeRef,typePath,desc,visible);
  }
  return null;
}
```
Original comment:
```
Visits an annotation on a type in the class signature.
```
Generated comment:
```
Visits an annotation on a local variable type.
```
---
id25
Code snippet:
```
public synchronized void ensureRestExpressRunning(boolean mockCassandra) throws IOException, IllegalAccessException, InstantiationException {
  if (restExpressRunning == false) {
    LOGGER.info(\"Starting RestExpress server...\");
    if (mockCassandra) {
      String[] params=new String[1];
      params[0]=\"local_test\";
      server=Main.initializeServer(params,null);
    }
 else {
      server=Main.initializeServer(new String[0],null);
    }
    restExpressRunning=true;
  }
}
```
Original comment:
```
Ensures RestExpress is presently running.
```
Generated comment:
```
Ensures that the given stream is not closed.
```
---
id26
Code snippet:
```
public static MatchedValuesFilter createApproximateFilter(String rawAttributeType,ByteString rawAssertionValue){
  Reject.ifNull(rawAttributeType,rawAssertionValue);
  return new MatchedValuesFilter(APPROXIMATE_MATCH_TYPE,rawAttributeType,rawAssertionValue,null,null,null,null);
}
```
Original comment:
```
Creates a new approxMatch filter with the provided information.
```
Generated comment:
```
Creates a new <code>attributesimpl</code> instance.
```
---
id27
Code snippet:
```
public boolean isReferral(){
  return hasObjectClassOrAttribute(OC_REFERRAL,ATTR_REFERRAL_URL);
}
```
Original comment:
```
Indicates whether this entry meets the criteria to consider it a referral (e.g., it contains the \"referral\" objectclass and a \"ref\" attribute).
```
Generated comment:
```
Returns whether it has the url.
```
---
id28
Code snippet:
```
public boolean move_drill_item(BrdAbit p_drill_item,PlaVectorInt p_vector,int p_max_recursion_depth,int p_max_via_recursion_depth,int p_pull_tight_accuracy,int p_pull_tight_time_limit){
  shove_fail_clear();
  Collection<BrdItem> contact_list=p_drill_item.get_normal_contacts();
  Iterator<BrdItem> it=contact_list.iterator();
  while (it.hasNext()) {
    BrdItem curr_contact=it.next();
    if (curr_contact.get_fixed_state() == ItemFixState.SHOVE_FIXED) {
      curr_contact.set_fixed_state(ItemFixState.UNFIXED);
    }
  }
  NetNosList net_no_arr=p_drill_item.net_nos;
  changed_area_clear();
  if (!move_drill_algo.insert(p_drill_item,p_vector,p_max_recursion_depth,p_max_via_recursion_depth,null)) {
    return false;
  }
  NetNosList opt_net_no_arr=p_max_recursion_depth <= 0 ? net_no_arr : NetNosList.EMPTY;
  TimeLimitStoppable t_limit=new TimeLimitStoppable(p_pull_tight_time_limit);
  changed_area_optimize(opt_net_no_arr,p_pull_tight_accuracy,null,t_limit,null);
  return true;
}
```
Original comment:
```
Translates p_drill_item by p_vector and shoves obstacle traces aside.  Returns false, if that was not possible without creating clearance violations.  In this case the database may be damaged, so that an undo becomes necessary.
```
Generated comment:
```
Moves an element to a new position.
```
---
id29
Code snippet:
```
public boolean equals(Object object){
  return (object != null && object instanceof IntegerSyntax && value == ((IntegerSyntax)object).value);
}
```
Original comment:
```
Returns whether this integer attribute is equivalent to the passed in object. To be equivalent, all of the following conditions must be true: <OL TYPE=1> <LI> <CODE>object</CODE> is not null. <LI> <CODE>object</CODE> is an instance of class IntegerSyntax. <LI> This integer attribute\'s value and <CODE>object</CODE>\'s value are equal. </OL>
```
Generated comment:
```
Compares this object to the specified object.
```
---
id30
Code snippet:
```
@Override public void toString(StringBuilder buffer){
  buffer.append(\"IntermediateResponse(oid=\").append(oid);
  if (value != null) {
    buffer.append(\", value=\").append(value);
  }
  buffer.append(\")\");
}
```
Original comment:
```
Appends a string representation of this LDAP protocol op to the provided buffer.
```
Generated comment:
```
Appends the specified response to this response.
```
---
id31
Code snippet:
```
public void uninstallUI(JComponent a){
  for (int i=0; i < uis.size(); i++) {
    ((ComponentUI)(uis.elementAt(i))).uninstallUI(a);
  }
}
```
Original comment:
```
Invokes the <code>uninstallUI</code> method on each UI handled by this object.
```
Generated comment:
```
Invokes the <code>uninstallui</code> method on each ui handled by this object.
```
---
id32
Code snippet:
```
public void internalFrameOpened(InternalFrameEvent e){
}
```
Original comment:
```
Invoked when an internal frame has been opened.
```
Generated comment:
```
Called when a new frame is removed.
```
---
id33
Code snippet:
```
void reset(){
  offset=intLen=0;
}
```
Original comment:
```
Set a MutableBigInteger to zero, removing its offset.
```
Generated comment:
```
Reset the chaining variables.
```
---
id34
Code snippet:
```
public final long determinant(PlaVectorInt p_other){
  return (long)v_x * p_other.v_y - (long)v_y * p_other.v_x;
}
```
Original comment:
```
Calculates the determinant of the matrix consisting of this Vector and p_other it is also the area between the two vectors
```
Generated comment:
```
Returns the distance from this int3d to the specified point. .
```
---
id35
Code snippet:
```
public void testClear() throws Exception {
  assertNull(cache.toVerboseString(),\"Expected empty cache.  \" + \"Cache contents:\" + ServerConstants.EOL + cache.toVerboseString());
  TestCaseUtils.initializeTestBackend(false);
  String b=DirectoryServer.getBackend(DN.valueOf(\"o=test\")).getBackendID();
  cache.clear();
  cache.putEntry(testEntriesList.get(0),b,1);
  cache.clear();
  assertNull(cache.getEntry(testEntriesList.get(0).getName()),\"Not expected to find \" + testEntriesList.get(0).getName() + \" in the cache.  Cache contents:\"+ ServerConstants.EOL+ cache.toVerboseString());
  assertNull(cache.getEntry(b,1),\"Not expected to find entry id \" + -1 + \" in the cache.  Cache contents:\"+ ServerConstants.EOL+ cache.toVerboseString());
  cache.clear();
}
```
Original comment:
```
Tests the <CODE>clear</CODE> method.
```
Generated comment:
```
Confirm that the local values average correctly back to the average value.
```
---
id36
Code snippet:
```
public void writeUint16(long n){
  check(2);
  buffer[write_pos++]=(byte)((n & 0x00ff00) >> 8);
  buffer[write_pos++]=(byte)(n & 0x00ff);
}
```
Original comment:
```
Writes Uint16 value
```
Generated comment:
```
Writes a long.
```
---
id37
Code snippet:
```
public static boolean isMarkup(int c){
  return c == \'<\' || c == \'&\' || c == \'%\';
}
```
Original comment:
```
Returns true if the specified character can be considered markup. Markup characters include \'&lt;\', \'&amp;\', and \'%\'.
```
Generated comment:
```
Returns true if the specified character is a letter.
```
---
id38
Code snippet:
```
public static void putFloat(String key,float value){
  if (mSharedPreferences == null) {
    return;
  }
  Editor editor=mSharedPreferences.edit();
  editor.putFloat(key,value);
  editor.apply();
}
```
Original comment:
```
Put a float value in the preferences editor.
```
Generated comment:
```
Inserts a float value into the mapping of this bundle, replacing any existing value for the given key. either key or value may be null.
```
---
id39
Code snippet:
```
public PrivilegedActionException(Exception exception){
  super((Throwable)null);
  this.exception=exception;
}
```
Original comment:
```
Constructs a new PrivilegedActionException &quot;wrapping&quot; the specific Exception.
```
Generated comment:
```
Constructs a new exception with the specified detail message, cause, and bean for jax-ws exception serialization.
```
---
id40
Code snippet:
```
@SuppressWarnings(\"unused\") public static long parseUnsignedInt(byte[] bytes){
  return parseUnsignedInt(bytes,0,bytes.length);
}
```
Original comment:
```
Parses an unsigned integers from a byte array.
```
Generated comment:
```
Parses a byte array from a byte array.
```
---
id41
Code snippet:
```
public void handleButton2Request(RequestInvocationEvent event){
  propertySheetModel.clear();
  populateValues=true;
  forwardTo();
}
```
Original comment:
```
Handles reset request.
```
Generated comment:
```
Handles the request to change the state of the button.
```
---
id42
Code snippet:
```
ArchiveException(String message,Exception cause){
  super(message,cause);
}
```
Original comment:
```
Construct an ArchiveException with a String and a cause
```
Generated comment:
```
Constructs a new exception with the specified detail message. the cause is not initialized.
```
---
id43
Code snippet:
```
public boolean isEmpty(){
  return true;
}
```
Original comment:
```
Implements for TaskRunnable interface, always return false.
```
Generated comment:
```
Returns <tt>true</tt> if this map contains no key-value mappings.
```
---
id44
Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  Node entRef;
  Node entText;
  Node createdNode;
  Node replacedChild;
  doc=(Document)load(\"staff\",true);
  entRef=doc.createEntityReference(\"ent4\");
  assertNotNull(\"createdEntRefNotNull\",entRef);
  entText=entRef.getFirstChild();
  createdNode=doc.createElement(\"newChild\");
{
    boolean success=false;
    try {
      replacedChild=entRef.replaceChild(createdNode,entText);
    }
 catch (    DOMException ex) {
      success=(ex.code == DOMException.NO_MODIFICATION_ALLOWED_ERR);
    }
    assertTrue(\"throw_NO_MODIFICATION_ALLOWED_ERR\",success);
  }
}
```
Original comment:
```
Runs the test case.
```
Generated comment:
```
Runs the test case.
```
---
id45
Code snippet:
```
public org.omg.PortableServer.Servant preinvoke(byte[] oid,org.omg.PortableServer.POA adapter,String operation,org.omg.PortableServer.ServantLocatorPackage.CookieHolder the_cookie) throws org.omg.PortableServer.ForwardRequest {
  org.omg.CORBA.portable.ServantObject $so=_servant_preinvoke(\"preinvoke\",_opsClass);
  ServantLocatorOperations $self=(ServantLocatorOperations)$so.servant;
  try {
    return $self.preinvoke(oid,adapter,operation,the_cookie);
  }
  finally {
    _servant_postinvoke($so);
  }
}
```
Original comment:
```
This operations is used to get a servant that will be used to process the request that caused preinvoke to be called.
```
Generated comment:
```
Invokes the specified httpclient method if it exists.
```
---
id46
Code snippet:
```
public boolean afterEveryday(OmniDate compareDate){
  return !beforeEveryday(compareDate);
}
```
Original comment:
```
only compare the hour minute and second
```
Generated comment:
```
Returns true if the given <code>uid</code> is <code>null</code>.
```
---
id47
Code snippet:
```
@Override public void execute() throws BuildException {
  super.execute();
  execute(createQueryString(\"/stop\").toString());
}
```
Original comment:
```
Execute the requested operation.
```
Generated comment:
```
Execute the query.
```
---
id48
Code snippet:
```
public com.sun.identity.liberty.ws.common.jaxb.ac.ActivationLimitDurationType createActivationLimitDurationType() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.liberty.ws.common.jaxb.ac.impl.ActivationLimitDurationTypeImpl();
}
```
Original comment:
```
Create an instance of ActivationLimitDurationType
```
Generated comment:
```
Creates a new activitymonitor.
```
---
id49
Code snippet:
```
public void change_side(PlaPointInt p_pole){
  on_front=!on_front;
  if (location != null)   location=location.mirror_vertical(p_pole);
}
```
Original comment:
```
Changes the placement side of this component and mirrors it at the vertical line through p_pole.
```
Generated comment:
```
Moves the specified point to the specified point in the specified direction.
```
---
id50
Code snippet:
```
public static String encodeLines(byte[] in){
  return encodeLines(in,0,in.length,76,systemLineSeparator);
}
```
Original comment:
```
Encodes a byte array into Base 64 format and breaks the output into lines of 76 characters. This method is compatible with <code>sun.misc.BASE64Encoder.encodeBuffer(byte[])</code>.
```
Generated comment:
```
Encodes a byte array into base 64 format and breaks the output into lines.
```
---
id51
Code snippet:
```
public ClearanceMatrix(int p_class_count,BrdLayerStructure p_layer_structure,String[] p_name_arr){
  class_count=Math.max(p_class_count,1);
  layer_structure=p_layer_structure;
  clearance_rows=new ClearanceMatrixRow[class_count];
  for (int index=0; index < class_count; ++index) {
    clearance_rows[index]=new ClearanceMatrixRow(this,p_name_arr[index]);
  }
  max_value_on_layer=new int[layer_structure.size()];
}
```
Original comment:
```
Creates a new instance for p_class_count clearance classes on p_layer_count layers. p_names is an array of dimension p_class_count;
```
Generated comment:
```
Construct a matrix from a one-dimensional array.
```
---
id52
Code snippet:
```
public void init(FilterConfig filterConfig){
  ServletContext cxt=filterConfig.getServletContext();
  Map<String,String> configData=new HashMap<String,String>();
  ResourceBundle res=ResourceBundle.getBundle(\"configparam\");
  for (Enumeration e=res.getKeys(); e.hasMoreElements(); ) {
    String key=(String)e.nextElement();
    String val=res.getString(key);
    configData.put(key,val);
  }
  EmbeddedOpenSSO embOpenSSO=new EmbeddedOpenSSO(cxt,System.getProperty(\"user.home\") + \"/\" + cxt.getContextPath(),configData);
  initialized=embOpenSSO.isConfigured();
  if (!initialized) {
    embOpenSSO.configure();
  }
  embOpenSSO.startup();
}
```
Original comment:
```
Initializes the filter.
```
Generated comment:
```
Initialize the filter.
```
---
id53
Code snippet:
```
static String generateRandomName(){
  StringBuilder sb=new StringBuilder(30);
  byte[] keyRandom=new byte[5];
  random.nextBytes(keyRandom);
  sb.append(currentTimeMillis()).toString();
  return (sb.append(Base64.encode(keyRandom)).toString());
}
```
Original comment:
```
Generates a random name for use in some policy elements. Note on using Random instead of SecureRandom in generating  random name:  names generated in this method are used for  policy elements Conditions, Referrals, Subjects, Rule  and Subjects if a name is not supplied by the caller.  Random is used to come up with a name that is not likely  to be used in the same policy.  These names are not meant to be secrets.  So, not a security problem.
```
Generated comment:
```
Generate a salt for use with the bcrypt.hashpw() method.
```
---
id54
Code snippet:
```
public void animateBgAlpha(float finalAlpha,int duration){
  int finalAlphaI=(int)(finalAlpha * 255f);
  if (getAlpha() != finalAlphaI) {
    mBackgroundAnim=cancelAnimator(mBackgroundAnim);
    mBackgroundAnim=ObjectAnimator.ofInt(this,\"alpha\",finalAlphaI);
    mBackgroundAnim.setDuration(duration);
    mBackgroundAnim.start();
  }
}
```
Original comment:
```
Animates the background alpha.
```
Generated comment:
```
Animates the rendering of the chart on the y-axis with the specified animation time. if animate(...) is called, no further calling of invalidate() is necessary to refresh the chart.
```
---
id55
Code snippet:
```
public DelegatingPreparedStatement(final DelegatingConnection<?> c,final PreparedStatement s){
  super(c,s);
}
```
Original comment:
```
Create a wrapper for the Statement which traces this Statement to the Connection which created it and the code which created it.
```
Generated comment:
```
This method was generated by mybatis generator. this method corresponds to the database table company.
```
---
id56
Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  Document newDoc;
  Element newElem;
  Document ownerDocDoc;
  Document ownerDocElem;
  DOMImplementation domImpl;
  DocumentType docType;
  String nullNS=null;
  doc=(Document)load(\"staff\",false);
  domImpl=doc.getImplementation();
  docType=domImpl.createDocumentType(\"mydoc\",nullNS,nullNS);
  newDoc=domImpl.createDocument(\"http://www.w3.org/DOM/Test\",\"mydoc\",docType);
  ownerDocDoc=newDoc.getOwnerDocument();
  assertNull(\"nodegetownerdocument02_1\",ownerDocDoc);
  newElem=newDoc.createElementNS(\"http://www.w3.org/DOM/Test\",\"myelem\");
  ownerDocElem=newElem.getOwnerDocument();
  assertNotNull(\"nodegetownerdocument02_2\",ownerDocElem);
}
```
Original comment:
```
Runs the test case.
```
Generated comment:
```
Runs the test case.
```
---
id57
Code snippet:
```
private static void disableConsoleLogging(final Logger logger){
  if (!\"true\".equalsIgnoreCase(System.getenv(\"OPENDJ_LOG_TO_STDOUT\"))) {
    logger.setUseParentHandlers(false);
  }
}
```
Original comment:
```
Prevents messages written to loggers from appearing in the console output.
```
Generated comment:
```
Disables logging for this logger.
```
---
id58
Code snippet:
```
public void writeRaw(byte b) throws IOException {
  _writeByte(b);
}
```
Original comment:
```
Method for directly inserting specified byte in output at current position. <p> NOTE: only use this method if you really know what you are doing.
```
Generated comment:
```
Writes a byte.
```
---
id59
Code snippet:
```
public SAXException(String message){
  super(message);
  this.exception=null;
}
```
Original comment:
```
Create a new SAXException.
```
Generated comment:
```
Constructs a new exception with the specified detail message. the cause is not initialized.
```
---
id60
Code snippet:
```
public void initializePersistence(Handler<AsyncResult<Void>> resultHandler){
  delegate.initializePersistence(resultHandler);
}
```
Original comment:
```
Initialize the persistence.
```
Generated comment:
```
Initialize the async service.
```
---
id61
Code snippet:
```
void attachView(){
  getPresenter().attachView(delegateCallback.getMvpView());
}
```
Original comment:
```
Attaches the view to the presenter
```
Generated comment:
```
Attaches the view to the view.
```
---
id62
Code snippet:
```
public String toString(){
  return (\"SAEPrincipal:  \" + name);
}
```
Original comment:
```
Returns a string representation of this <code>SAEPrincipal</code>. <p>
```
Generated comment:
```
String representation.
```
---
id63
Code snippet:
```
private static void addItemsToList(int startIndex,int endIndex){
  for (int i=startIndex; i < endIndex; i++) {
    values.add(new Integer(i));
  }
}
```
Original comment:
```
Adds the items to the list. Items added to the list are numbers and letters.
```
Generated comment:
```
Add an item to the list.
```
---
id64
Code snippet:
```
@Override public void write(byte[] buffer) throws IOException {
  write(buffer,0,buffer.length);
}
```
Original comment:
```
Equivalent to calling write(buffer, 0, buffer.length).
```
Generated comment:
```
Writes a byte array to the output stream.
```
---
id65
Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(hc_attrcreatetextnode.class,args);
}
```
Original comment:
```
Runs this test from the command line.
```
Generated comment:
```
Runs this test from the command line.
```
---
id66
Code snippet:
```
public Builder add(String name,String value){
  checkNameAndValue(name,value);
  return addLenient(name,value);
}
```
Original comment:
```
Add a field with the specified value.
```
Generated comment:
```
Adds a value to the set.
```
---
id67
Code snippet:
```
public void handleAdvancedOptionButtonRequest(RequestInvocationEvent event) throws ModelControlException {
  CoreAttributesViewBean vb=(CoreAttributesViewBean)getViewBean(CoreAttributesViewBean.class);
  unlockPageTrail();
  passPgSessionMap(vb);
  vb.forwardTo(getRequestContext());
}
```
Original comment:
```
Handles new authentication configuration request.
```
Generated comment:
```
This method is called when a new button is pressed.
```
---
id68
Code snippet:
```
static long readEpochSec(DataInput in) throws IOException {
  int hiByte=in.readByte() & 255;
  if (hiByte == 255) {
    return in.readLong();
  }
 else {
    int midByte=in.readByte() & 255;
    int loByte=in.readByte() & 255;
    long tot=((hiByte << 16) + (midByte << 8) + loByte);
    return (tot * 900) - 4575744000L;
  }
}
```
Original comment:
```
Reads the state from the stream.
```
Generated comment:
```
Reads a long natural number in &zeta; coding.
```
---
id69
Code snippet:
```
public static Object unmarshal(String data) throws Exception {
  if (data.startsWith(TOKEN_PREFIX)) {
    return SSOTokenManager.getInstance().createSSOToken(data.substring(TOKEN_PREFIX.length()));
  }
 else   if (data.startsWith(OBJECT_PREFIX)) {
    return IOUtils.deserialise(Base64.decode(data.substring(OBJECT_PREFIX.length())),false);
  }
 else {
    throw new IllegalArgumentException(\"Bad context value:\" + data);
  }
}
```
Original comment:
```
Deserialize the context from the string created by previous call to marshal()
```
Generated comment:
```
Decodes a quoted-printable object into its original form. escaped characters are converted back to their original representation.
```
---
id70
Code snippet:
```
public Random(){
  setSeed(System.currentTimeMillis() + System.identityHashCode(this));
}
```
Original comment:
```
Constructs a random generator with an initial state that is unlikely to be duplicated by a subsequent instantiation. <p>The initial state (that is, the seed) is <i>partially</i> based on the current time of day in milliseconds.
```
Generated comment:
```
Creates a new instance.
```
---
id71
Code snippet:
```
public static boolean isTeslaProducer(ICapabilityProvider provider,EnumFacing side){
  return provider.hasCapability(TeslaCapabilities.CAPABILITY_PRODUCER,side);
}
```
Original comment:
```
Checks if a capability provider is a Tesla producer.
```
Generated comment:
```
Checks whether the given capability is available.
```
---
id72
Code snippet:
```
public AcceptLanguageHeader createAcceptLanguageHeader(Locale language){
  if (language == null)   throw new NullPointerException(\"null arg\");
  AcceptLanguage acceptLanguage=new AcceptLanguage();
  acceptLanguage.setAcceptLanguage(language);
  return acceptLanguage;
}
```
Original comment:
```
Creates a new AcceptLanguageHeader based on the newly supplied language value.
```
Generated comment:
```
Creates a new languageheader based on the newly supplied language value.
```
---
id73
Code snippet:
```
private void switchRecordLayout(boolean recordingMode){
  ActionBar actionBar=getActionBar();
  invalidateOptionsMenu();
  actionBar.setDisplayHomeAsUpEnabled(recordingMode);
  actionBar.setHomeButtonEnabled(recordingMode);
  actionBar.setTitle(recordingMode ? R.string.fm_recorder_name : R.string.app_name);
  LinearLayout recBar=(LinearLayout)findViewById(R.id.bottom_bar_recorder);
  LinearLayout bottomBar=(LinearLayout)findViewById(R.id.bottom_bar);
  bottomBar.setVisibility(recordingMode ? View.GONE : View.VISIBLE);
  recBar.setVisibility(recordingMode ? View.VISIBLE : View.GONE);
  mButtonAddToFavorite.setVisibility(recordingMode ? View.GONE : View.VISIBLE);
}
```
Original comment:
```
Switch to record layout, if in recorder mode.
```
Generated comment:
```
Toggle the mute state of the slider.
```
---
id74
Code snippet:
```
protected void readFDSelect(int Font){
  int NumOfGlyphs=fonts[Font].nglyphs;
  int[] FDSelect=new int[NumOfGlyphs];
  seek(fonts[Font].fdselectOffset);
  fonts[Font].FDSelectFormat=getCard8();
switch (fonts[Font].FDSelectFormat) {
case 0:
    for (int i=0; i < NumOfGlyphs; i++) {
      FDSelect[i]=getCard8();
    }
  fonts[Font].FDSelectLength=fonts[Font].nglyphs + 1;
break;
case 3:
int nRanges=getCard16();
int l=0;
int first=getCard16();
for (int i=0; i < nRanges; i++) {
int fd=getCard8();
int last=getCard16();
int steps=last - first;
for (int k=0; k < steps; k++) {
FDSelect[l]=fd;
l++;
}
first=last;
}
fonts[Font].FDSelectLength=1 + 2 + nRanges * 3 + 2;
break;
default :
break;
}
fonts[Font].FDSelect=FDSelect;
}
```
Original comment:
```
Read the FDSelect of the font and compute the array and its length
```
Generated comment:
```
Reads the font from the specified font.
```
---
id75
Code snippet:
```
public void delete() throws IOException {
  close();
  Util.deleteContents(directory);
}
```
Original comment:
```
Closes the cache and deletes all of its stored values. This will delete all files in the cache directory including files that weren\'t created by the cache.
```
Generated comment:
```
Closes the cache and deletes all of its stored values. this will delete all files in the cache directory including files that weren\'t created by the cache.
```
---
id76
Code snippet:
```
protected void tearDown(){
}
```
Original comment:
```
Tears down the fixture, for example, close a network connection. This method is called after a test is executed.
```
Generated comment:
```
Tears down the fixture, for example, close a network connection. this method is called after a test is executed.
```
---
id77
Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  DocumentType docType;
  NamedNodeMap entityList;
  Entity entityNode;
  String publicId;
  doc=(Document)load(\"staff\",false);
  docType=doc.getDoctype();
  assertNotNull(\"docTypeNotNull\",docType);
  entityList=docType.getEntities();
  assertNotNull(\"entitiesNotNull\",entityList);
  entityNode=(Entity)entityList.getNamedItem(\"ent1\");
  publicId=entityNode.getPublicId();
  assertNull(\"entityGetPublicIdNullAssert\",publicId);
}
```
Original comment:
```
Runs the test case.
```
Generated comment:
```
Runs the test case.
```
---
id78
Code snippet:
```
@Override public R visitVariable(VariableElement e,P p){
  return scan(e.getEnclosedElements(),p);
}
```
Original comment:
```
This implementation scans the enclosed elements.
```
Generated comment:
```
Visits the given type-specific ast node. <p> the default implementation does nothing. subclasses may reimplement. </p>.
```
---
id79
Code snippet:
```
public com.sun.identity.saml2.jaxb.metadata.AttributeServiceType createAttributeServiceType() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.saml2.jaxb.metadata.impl.AttributeServiceTypeImpl();
}
```
Original comment:
```
Create an instance of AttributeServiceType
```
Generated comment:
```
Returns a new instance of the attribute.
```
---
id80
Code snippet:
```
public org.omg.DynamicAny.DynAny current_component() throws org.omg.DynamicAny.DynAnyPackage.TypeMismatch {
  org.omg.CORBA.portable.ServantObject $so=_servant_preinvoke(\"current_component\",_opsClass);
  DynFixedOperations $self=(DynFixedOperations)$so.servant;
  try {
    return $self.current_component();
  }
  finally {
    _servant_postinvoke($so);
  }
}
```
Original comment:
```
Returns the DynAny for the component at the current position. It does not advance the current position, so repeated calls to current_component without an intervening call to rewind, next, or seek return the same component. The returned DynAny object reference can be used to get/set the value of the current component. If the current component represents a complex type, the returned reference can be narrowed based on the TypeCode to get the interface corresponding to the to the complex type. Calling current_component on a DynAny that cannot have components, such as a DynEnum or an empty exception, raises TypeMismatch. Calling current_component on a DynAny whose current position is -1 returns a nil reference. The iteration operations, together with current_component, can be used to dynamically compose an any value. After creating a dynamic any, such as a DynStruct, current_component and next can be used to initialize all the components of the value. Once the dynamic value is completely initialized, to_any creates the corresponding any value.
```
Generated comment:
```
Invokes the <code>getinstance</code> method on each ui handled by this object.
```
---
id81
Code snippet:
```
public static void write(AudioFile f) throws CannotWriteException {
  getDefaultAudioFileIO().writeFile(f);
}
```
Original comment:
```
Write the tag contained in the audioFile in the actual file on the disk.
```
Generated comment:
```
Write a file.
```
---
id82
Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList elementList;
  Node employeeNode;
  NodeList childList;
  Node oldChild;
  Node newChild;
  Node child;
  String childName;
  Node replacedNode;
  doc=(Document)load(\"hc_staff\",true);
  elementList=doc.getElementsByTagName(\"p\");
  employeeNode=elementList.item(1);
  childList=employeeNode.getChildNodes();
  oldChild=childList.item(0);
  newChild=doc.createElement(\"br\");
  replacedNode=employeeNode.replaceChild(newChild,oldChild);
  child=childList.item(0);
  childName=child.getNodeName();
  assertEqualsAutoCase(\"element\",\"nodeName\",\"br\",childName);
}
```
Original comment:
```
Runs the test case.
```
Generated comment:
```
Runs the test case.
```
---
id83
Code snippet:
```
protected boolean end(TextView widget,Spannable buffer){
  return false;
}
```
Original comment:
```
Performs an end movement action. Moves the cursor or scrolls to the start of the line or to the top of the document depending on whether the insertion point is being moved or the document is being scrolled.
```
Generated comment:
```
Performs a scroll to top action. scrolls to the bottom of the document.
```
---
id84
Code snippet:
```
private synchronized void seekToCurrentValue() throws IOException {
  valBuffer.reset();
}
```
Original comment:
```
Position valLenIn/valIn to the \'value\' corresponding to the \'current\' key
```
Generated comment:
```
Reset the stream.
```
---
id85
Code snippet:
```
public final DetectorResult detect(Map<DecodeHintType,?> hints) throws NotFoundException, FormatException {
  resultPointCallback=hints == null ? null : (ResultPointCallback)hints.get(DecodeHintType.NEED_RESULT_POINT_CALLBACK);
  FinderPatternFinder finder=new FinderPatternFinder(image,resultPointCallback);
  FinderPatternInfo info=finder.find(hints);
  return processFinderPatternInfo(info);
}
```
Original comment:
```
<p>Detects a QR Code in an image.</p>
```
Generated comment:
```
<p>detects a qr code in an image.</p>.
```
---
id86
Code snippet:
```
public static boolean isName(int c){
  return c < 0x10000 && (CHARS[c] & MASK_NAME) != 0;
}
```
Original comment:
```
Returns true if the specified character is a valid name character as defined by production [4] in the XML 1.0 specification.
```
Generated comment:
```
Returns true if the specified character is a valid ncname character as defined by production [4] in the xml 1.0 specification.
```
---
id87
Code snippet:
```
private void onTLMessage(@NotNull TLMessage message){
  if (message.hasFromId()) {
    final IUser user=databaseManager.getUserById(message.getFromId());
    if (user != null) {
      this.tlMessageHandler.onTLMessage(message);
    }
  }
}
```
Original comment:
```
Handles TLMessage
```
Generated comment:
```
Called when a message is received.
```
---
id88
Code snippet:
```
public WrappedPlainView(Element elem,boolean wordWrap){
  super(elem,Y_AXIS);
  this.wordWrap=wordWrap;
}
```
Original comment:
```
Creates a new WrappedPlainView.  Lines can be wrapped on either character or word boundaries depending upon the setting of the wordWrap parameter.
```
Generated comment:
```
Creates a new view.
```
---
id89
Code snippet:
```
public InvalidAttributeValueException(){
  super();
}
```
Original comment:
```
Constructs an <code>InvalidAttributeValueException</code> with no specified detail message.
```
Generated comment:
```
Constructs a new exception with <code>null</code> as its detail message. the cause is not initialized.
```
---
id90
Code snippet:
```
public void removeDefaultValues() throws SMSException, SSOException {
  updateDefaultValues(new HashSet());
}
```
Original comment:
```
Removes the all the default values for the attribute.
```
Generated comment:
```
Removes a value from the table.
```
---
id91
Code snippet:
```
public SQLDataException(Throwable cause){
  super(cause);
}
```
Original comment:
```
Creates an SQLDataException object. The Reason string is set to the null if cause == null or cause.toString() if cause!=null,and the cause Throwable object is set to the given cause Throwable object.
```
Generated comment:
```
Creates an sqldataexception object. the reason string is set to the given reason string, the sqlstate string is set to the given cause throwable object.
```
---
id92
Code snippet:
```
public void traverse(Node pos) throws org.xml.sax.SAXException {
  this.m_contentHandler.startDocument();
  traverseFragment(pos);
  this.m_contentHandler.endDocument();
}
```
Original comment:
```
Perform a pre-order traversal non-recursive style.   Note that TreeWalker assumes that the subtree is intended to represent  a complete (though not necessarily well-formed) document and, during a  traversal, startDocument and endDocument will always be issued to the  SAX listener.
```
Generated comment:
```
Perform a pre-order traversal non-recursive style. note that treewalker assumes that the subtree is intended to represent a complete (though not necessarily well-formed) document and, during a traversal, startdocument and enddocument will always be issued to the sax listener.
```
---
id93
Code snippet:
```
private void importListeners(Map<String,EntryListeners> listenersCopy,Schema schema){
  for (  Map.Entry<String,EntryListeners> entry : listenersCopy.entrySet()) {
    listeners.put(DN.valueOf(entry.getKey(),schema),entry.getValue());
  }
}
```
Original comment:
```
Imports the provided listeners into the configuration handler.
```
Generated comment:
```
Imports the schema.
```
---
id94
Code snippet:
```
@Override public void endAccess(){
  isNew=false;
  if (LAST_ACCESS_AT_START) {
    this.lastAccessedTime=this.thisAccessedTime;
    this.thisAccessedTime=System.currentTimeMillis();
  }
 else {
    this.thisAccessedTime=System.currentTimeMillis();
    this.lastAccessedTime=this.thisAccessedTime;
  }
  if (ACTIVITY_CHECK) {
    accessCount.decrementAndGet();
  }
}
```
Original comment:
```
End the access.
```
Generated comment:
```
Decrements the clock.
```
---
id95
Code snippet:
```
public String toStringImpl(){
  return id;
}
```
Original comment:
```
Used by super class to log the attribute\'s contents when packet logging is enabled.
```
Generated comment:
```
Returns a string representation of this object.
```
---
id96
Code snippet:
```
@Override public int hashCode(){
  return attribute.hashCode();
}
```
Original comment:
```
Retrieves the hash code for this modification.  The hash code returned will be the hash code for the attribute included in this modification.
```
Generated comment:
```
Returns a hash code for this instance.
```
---
id97
Code snippet:
```
void toString(final StringBuilder buffer){
  boolean first=true;
  for (  CSN csn : serverIdToCSN.values()) {
    if (!first) {
      buffer.append(\" \");
    }
    csn.toString(buffer);
    first=false;
  }
}
```
Original comment:
```
Appends the text representation of ServerState.
```
Generated comment:
```
Appends the given string to the buffer.
```
---
id98
Code snippet:
```
public StringBuilder encodeBody(StringBuilder retval){
  if (callId == null)   return retval;
 else {
    retval.append(callId);
    if (!parameters.isEmpty()) {
      retval.append(SEMICOLON);
      parameters.encode(retval);
    }
    return retval;
  }
}
```
Original comment:
```
Encode the body part of this header (i.e. leave out the hdrName).
```
Generated comment:
```
Encode the body of the header.
```
---
id99
Code snippet:
```
private void playJumpTrailEffect(){
  if (opacity > 0) {
    sMario.getJumpEffect().setOpacity(opacity);
    sMario.getJumpTrail().setOpacity(opacity);
    sMario.getJumpTrail().setFitHeight(sMario.getJumpTrail().getFitHeight() + (opacity * jumpTrailHeightDelta));
    sMario.getJumpTrail().setTranslateY(sMario.getJumpTrail().getTranslateY() - (opacity * jumpTrailHeightDelta));
    opacity-=0.06;
  }
}
```
Original comment:
```
Plays Mario\'s jump effect sequence.
```
Generated comment:
```
Plays the sound.
```
---
id100
Code snippet:
```
public void destroy(Session requester,Session session) throws SessionException {
  if (debug.messageEnabled()) {
    debug.message(MessageFormat.format(\"Remote destroy {0}\",session));
  }
  SessionRequest sreq=new SessionRequest(SessionRequest.DestroySession,requester.getID().toString(),false);
  sreq.setDestroySessionID(session.getID().toString());
  requests.sendRequestWithRetry(session.getSessionServiceURL(),sreq,session);
}
```
Original comment:
```
Destroys the Session via the Session remote service URL.
```
Generated comment:
```
Destroy a session.
```
---
id101
Code snippet:
```
public String toXML(){
  StringBuilder stringBuilder=new StringBuilder();
  return stringBuilder.toString();
}
```
Original comment:
```
Default toXML Method to Marshal Object into XML.
```
Generated comment:
```
Returns a string representation of this object.
```
---
id102
Code snippet:
```
@Override public String toString(){
  return buf.toString();
}
```
Original comment:
```
Returns the signature that was built by this signature writer.
```
Generated comment:
```
Returns a string representation of this object.
```
---
id103
Code snippet:
```
public FrameBodyTCOP(){
}
```
Original comment:
```
Creates a new FrameBodyTCOP datatype.
```
Generated comment:
```
Creates a new instance.
```
---
id104
Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(namednodemapgetnameditem.class,args);
}
```
Original comment:
```
Runs this test from the command line.
```
Generated comment:
```
Runs this test from the command line.
```
---
id105
Code snippet:
```
public static <S>ServiceLoader<S> load(Class<S> service,ClassLoader loader){
  return new ServiceLoader<>(service,loader);
}
```
Original comment:
```
Creates a new service loader for the given service type and class loader.
```
Generated comment:
```
Creates a new service loader.
```
---
id106
Code snippet:
```
@SuppressWarnings(\"unused\") static <T>ReplayPromise<Set<T>> replayPromiseSet(Class<T> componentType,final Duration timeout,final long time){
  return new ReplayPromiseImpl<>(timeout,time);
}
```
Original comment:
```
Generic set promise. Added to make static imports possible.
```
Generated comment:
```
Create a lazypstackx.
```
---
id107
Code snippet:
```
private GroovyShell $getShell(){
  return CpsThreadGroup.current().getExecution().getShell();
}
```
Original comment:
```
Obtains the Groovy compiler to be used for compiling user script in the CPS-transformed and sandboxed manner.
```
Generated comment:
```
Returns a new instance of this phase. this phase contains no per-compilation instance fields.
```
---
id108
Code snippet:
```
private void updateAttrInConfig(BaseConfigType baseConfig,Map values,String role) throws JAXBException, AMConsoleException {
  List attrList=baseConfig.getAttribute();
  if (role.equals(EntityModel.IDENTITY_PROVIDER)) {
    attrList.clear();
    baseConfig=addAttributeType(getAllIDPExtendedMetaMap(),baseConfig);
    attrList=baseConfig.getAttribute();
  }
 else   if (role.equals(EntityModel.SERVICE_PROVIDER)) {
    attrList.clear();
    baseConfig=addAttributeType(getAllSPExtendedMetaMap(),baseConfig);
    attrList=baseConfig.getAttribute();
  }
  for (Iterator it=attrList.iterator(); it.hasNext(); ) {
    AttributeElement avpnew=(AttributeElement)it.next();
    String name=avpnew.getName();
    if (values.keySet().contains(name)) {
      Set set=(Set)values.get(name);
      if (set != null) {
        avpnew.getValue().clear();
        avpnew.getValue().addAll(set);
      }
    }
  }
}
```
Original comment:
```
Updates the BaseConfigElement.
```
Generated comment:
```
Updates the configuration of the given element.
```
---
id109
Code snippet:
```
private boolean isLicenseAccepted(){
  return Boolean.parseBoolean(getContext().getRequestParameter(SetupConstants.ACCEPT_LICENSE_PARAM));
}
```
Original comment:
```
Checks whether the user has accepted the terms of the license agreement.
```
Generated comment:
```
Returns true if the user is currently running.
```
---
id110
Code snippet:
```
public void scroll(int itemsToScroll,int time){
  int distance=itemsToScroll * getItemHeight() - scrollingOffset;
  scroller.scroll(distance,time);
}
```
Original comment:
```
Scroll the wheel
```
Generated comment:
```
Scrolls the view by the specified amount.
```
---
id111
Code snippet:
```
@DataProvider public Object[][] testBindData(){
  return new Object[][]{{false,false},{false,true},{true,false},{true,true}};
}
```
Original comment:
```
Returns test data for the simple/sasl tests.
```
Generated comment:
```
This method was generated by mybatis generator. this method corresponds to the database table iteration.
```
---
id112
Code snippet:
```
void markInProgress(LDAPUpdateMsg msg){
  remotePendingChanges.markInProgress(msg);
}
```
Original comment:
```
Marks the specified message as the one currently processed by a replay thread.
```
Generated comment:
```
Marks the current position in the list.
```
---
id113
Code snippet:
```
private void assertion(boolean b,String msg){
  if (!b) {
    String fMsg=XSLMessages.createXPATHMessage(XPATHErrorResources.ER_INCORRECT_PROGRAMMER_ASSERTION,new Object[]{msg});
    throw new RuntimeException(fMsg);
  }
}
```
Original comment:
```
Notify the user of an assertion error, and probably throw an exception.
```
Generated comment:
```
Send a debug log message.
```
---
id114
Code snippet:
```
public BarcodeEANSUPP(Barcode1D ean,Barcode1D supp){
  super(ean.document);
  n=8;
  this.ean=ean;
  this.supp=supp;
}
```
Original comment:
```
Creates new combined barcode.
```
Generated comment:
```
Creates a new instance.
```
---
id115
Code snippet:
```
public ServicesAddViewBean(){
  super(\"ServicesAdd\",DEFAULT_DISPLAY_URL,null);
  String serviceName=(String)getPageSessionAttribute(SERVICE_NAME);
  if (serviceName != null) {
    initialize(serviceName);
  }
}
```
Original comment:
```
Creates a service profile view bean.
```
Generated comment:
```
Creates a new instance of the switch. <!-- begin-user-doc --> <!-- end-user-doc -->.
```
---
id116
Code snippet:
```
@Override public void removeByField2(boolean field2){
  for (  Foo foo : findByField2(field2,QueryUtil.ALL_POS,QueryUtil.ALL_POS,null)) {
    remove(foo);
  }
}
```
Original comment:
```
Removes all the foos where field2 = &#63; from the database.
```
Generated comment:
```
Removes the specified field from the query.
```
---
id117
Code snippet:
```
final void nextStream() throws IOException {
  if (in != null) {
    in.close();
  }
  if (e.hasMoreElements()) {
    in=(InputStream)e.nextElement();
    if (in == null)     throw new NullPointerException();
  }
 else   in=null;
}
```
Original comment:
```
Continues reading in the next stream if an EOF is reached.
```
Generated comment:
```
See the general contract of the <code>readfully</code> method of <code>inputstream</code>. <p> bytes for this operation are read from the contained input stream.
```
---
id118
Code snippet:
```
public static void assertColumnTypes(ResultSet rs,int[] expectedTypes) throws SQLException {
  ResultSetMetaData rsmd=rs.getMetaData();
  int actualCols=rsmd.getColumnCount();
  assertEquals(\"Unexpected column count:\",expectedTypes.length,rsmd.getColumnCount());
  for (int i=0; i < actualCols; i++) {
    assertEquals(\"Column types do not match for column \" + (i + 1),expectedTypes[i],rsmd.getColumnType(i + 1));
  }
}
```
Original comment:
```
Test Method from Apache Derby Project Class org.apache.derbyTesting.functionTests.tests.jdbcapi.DatabaseMetaDataTest Takes a result set and an array of expected column types from java.sql.Types and asserts that the column types in the result set metadata match the number, order, and names of those in the array. No length information for variable length types can be passed. For ResultSets from JDBC DatabaseMetaData the specification only indicates the types of the columns, not the length.
```
Generated comment:
```
Check if two result sets are equal.
```
---
id119
Code snippet:
```
public String nextToken(){
  if (currentPosition >= maxPosition) {
    throw new NoSuchElementException();
  }
  int start=currentPosition;
  while ((currentPosition < maxPosition) && Character.isLetterOrDigit(str.charAt(currentPosition))) {
    currentPosition++;
  }
  if ((start == currentPosition) && (!Character.isLetterOrDigit(str.charAt(currentPosition)))) {
    currentPosition++;
  }
  return str.substring(start,currentPosition);
}
```
Original comment:
```
Returns the next token from this string tokenizer.
```
Generated comment:
```
Returns the next token in the string.
```
---
id120
Code snippet:
```
public void testEngineGenerateCertPathLjava_io_InputStream_Ljava_lang_String02(){
  CertificateFactorySpi certFactorySpi=new extCertificateFactorySpi();
  ByteArrayInputStream bais=new ByteArrayInputStream(new byte[0]);
  DataInputStream dis=new DataInputStream(bais);
  try {
    certFactorySpi.engineGenerateCertPath(dis,\"encoding\");
    fail(\"UnsupportedOperationException expected\");
  }
 catch (  UnsupportedOperationException e) {
  }
catch (  CertificateException e) {
    fail(\"Unexpected CertificateException \" + e.getMessage());
  }
}
```
Original comment:
```
Test for <code>engineGenerateCertPath(InputStream, String)</code> method. Assertion: generates a <code>CertPath</code> object and initializes it with the data read from the <code>InputStream</code>
```
Generated comment:
```
Test for <code>getinstance(string type, string provider)</code> method assertion: throws nullpointerexception when type is null.
```
---
id121
Code snippet:
```
BigInteger copy(){
  prepareJavaRepresentation();
  int[] copyDigits=new int[numberLength];
  System.arraycopy(digits,0,copyDigits,0,numberLength);
  return new BigInteger(sign,numberLength,copyDigits);
}
```
Original comment:
```
Returns a copy of the current instance to achieve immutability
```
Generated comment:
```
Generate a random biginteger.
```
---
id122
Code snippet:
```
public PathHeader createPathHeader(Address address){
  if (address == null)   throw new NullPointerException(\"null address!\");
  Path path=new Path();
  path.setAddress(address);
  return path;
}
```
Original comment:
```
PATH header
```
Generated comment:
```
Creates a new loconet header based on the newly supplied address value.
```
---
id123
Code snippet:
```
public boolean beginStaticTextExceptionDisplay(ChildDisplayEvent event){
  return true;
}
```
Original comment:
```
Returns if it begins static text exception display
```
Generated comment:
```
Returns true if the given window is visible.
```
---
id124
Code snippet:
```
private void appendErrorLine(String msg){
  msg=filterForBugID4988885(msg + \"<br>\");
  msg=Utilities.applyFont(msg,ColorAndFontConstants.progressFont);
  appendHtml(msg);
}
```
Original comment:
```
Appends a line to the logs (Details are) section of the panel.  The text will have a new-line char at the end (is similar to println()).
```
Generated comment:
```
Appends the error message to the message.
```
---
id125
Code snippet:
```
public URI toURI() throws URISyntaxException {
  return new URI(toExternalForm());
}
```
Original comment:
```
Returns the URI equivalent to this URL.
```
Generated comment:
```
Converts a uri to a uri.
```
---
id126
Code snippet:
```
private void validateSourceAndDestinationServersOptions(LocalizableMessageBuilder buf){
  if (hostNameSourceArg.getValue().equalsIgnoreCase(hostNameDestinationArg.getValue()) && !isInteractive() && portSourceArg.getValue().equals(portDestinationArg.getValue())) {
    LocalizableMessage message=ERR_SOURCE_DESTINATION_INITIALIZE_SAME_SERVER_PORT.get(hostNameSourceArg.getValue(),portSourceArg.getValue());
    addMessage(buf,message);
  }
}
```
Original comment:
```
Checks the initialize replication subcommand options and updates the provided LocalizableMessageBuilder with the errors that were encountered with the subcommand options. This method assumes that the method parseArguments for the parser has already been called.
```
Generated comment:
```
Validates that the host is valid.
```
---
id127
Code snippet:
```
public LDAPAttribute(String attributeType,String value){
  this.attributeType=attributeType;
  values=newArrayList(ByteString.valueOfUtf8(value));
}
```
Original comment:
```
Creates a new LDAP attribute with the provided type and no values.
```
Generated comment:
```
Creates a new attribute.
```
---
id128
Code snippet:
```
public static NodeList selectNodeList(Node doc,String str,NamespaceContext nsctx) throws XPathException {
  XPathFactory xpf=xpathFactoryCache.getInstanceForCurrentThread();
  XPath xpath=xpf.newXPath();
  xpath.setNamespaceContext(nsctx);
  XPathExpression expr=xpath.compile(str);
  return (NodeList)expr.evaluate(doc,XPathConstants.NODESET);
}
```
Original comment:
```
Use an XPath string to select a nodelist Namespace prefix is resolved using the the specified context.
```
Generated comment:
```
Use an xpath string to select a nodelist. xpath namespace prefixes are resolved from the namespacenode.
```
---
id129
Code snippet:
```
public NotConfiguration(String message,Throwable cause){
  super(message,cause);
}
```
Original comment:
```
Constructs a new exception with the specified detail message and cause.
```
Generated comment:
```
Constructs a new exception with the specified detail message, cause, and bean for jax-ws exception serialization.
```
---
id130
Code snippet:
```
public static MethodNode generateSetter(String methodName,String fieldName,String className,String fieldDesc){
  MethodNode methodNode=new MethodNode(ACC_PUBLIC,methodName,\"(\" + fieldDesc + \")V\",null,null);
  methodNode.instructions.insert(new VarInsnNode(ALOAD,0));
  methodNode.instructions.insert(new VarInsnNode(Type.getType(fieldDesc).getOpcode(ILOAD),1));
  methodNode.instructions.insert(new FieldInsnNode(PUTFIELD,className,fieldName,fieldDesc));
  methodNode.instructions.insert(new InsnNode(RETURN));
  return methodNode;
}
```
Original comment:
```
Generates a setter method for the specified field
```
Generated comment:
```
Generates code for the given return type.
```
---
id131
Code snippet:
```
public FSAuthDomainsEditViewBean(){
  super(\"FSAuthDomainsEdit\");
  setDefaultDisplayURL(DEFAULT_DISPLAY_URL);
}
```
Original comment:
```
Creates a authentication domains creation view bean.
```
Generated comment:
```
Constructs a new exception with <code>null</code> as its detail message. the cause is not initialized.
```
---
id132
Code snippet:
```
public boolean isInverted(){
  return ((getData() & 0x8) != 0);
}
```
Original comment:
```
Test if step is inverted
```
Generated comment:
```
Gets the value of the ipv6 property.
```
---
id133
Code snippet:
```
private void componentChanged(JComponent c){
  JComponent comp=((JToolTip)c).getComponent();
  if (comp != null && !(comp.isEnabled())) {
    if (UIManager.getBorder(\"ToolTip.borderInactive\") != null) {
      LookAndFeel.installBorder(c,\"ToolTip.borderInactive\");
    }
 else {
      LookAndFeel.installBorder(c,\"ToolTip.border\");
    }
    if (UIManager.getColor(\"ToolTip.backgroundInactive\") != null) {
      LookAndFeel.installColors(c,\"ToolTip.backgroundInactive\",\"ToolTip.foregroundInactive\");
    }
 else {
      LookAndFeel.installColors(c,\"ToolTip.background\",\"ToolTip.foreground\");
    }
  }
 else {
    LookAndFeel.installBorder(c,\"ToolTip.border\");
    LookAndFeel.installColors(c,\"ToolTip.background\",\"ToolTip.foreground\");
  }
}
```
Original comment:
```
Invoked when the <code>JCompoment</code> associated with the <code>JToolTip</code> has changed, or at initialization time. This should update any state dependant upon the <code>JComponent</code>.
```
Generated comment:
```
Invokes the <code>uninstallui</code> method on each ui handled by this object.
```
---
id134
Code snippet:
```
public com.sun.identity.wsfederation.jaxb.wsaddr.FaultToElement createFaultToElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.wsfederation.jaxb.wsaddr.impl.FaultToElementImpl();
}
```
Original comment:
```
Create an instance of FaultToElement
```
Generated comment:
```
Adds an element to the element.
```
---
id135
Code snippet:
```
@CpsVmThreadOnly private void propagateErrorToWorkflow(Throwable t){
  Map.Entry<Integer,CpsThread> lastEntry=threads.lastEntry();
  if (lastEntry != null) {
    lastEntry.getValue().resume(new Outcome(null,t));
  }
 else {
    LOGGER.log(Level.WARNING,\"encountered error but could not pass it to the flow\",t);
  }
}
```
Original comment:
```
Propagates the failure to the workflow by passing an exception
```
Generated comment:
```
Abort the worker thread.
```
---
id136
Code snippet:
```
public static ExtOp decode(EnumTargetOperator operator,String expr) throws AciException {
  Set<String> extOpOIDs=Aci.decodeOID(expr,WARN_ACI_SYNTAX_INVALID_TARGEXTOP_EXPRESSION.get(expr));
  return new ExtOp(operator,extOpOIDs);
}
```
Original comment:
```
Decode an extop expression string.
```
Generated comment:
```
Performs a binary decoding operation.
```
---
id137
Code snippet:
```
private static String matchablePath(String path){
  if (path == null) {
    return \"/\";
  }
 else   if (path.endsWith(\"/\")) {
    return path;
  }
 else {
    return path + \"/\";
  }
}
```
Original comment:
```
Returns a non-null path ending in \"/\".
```
Generated comment:
```
Returns the path of the path.
```
---
id138
Code snippet:
```
int findAncestor(XPathContext xctxt,XPath fromMatchPattern,XPath countMatchPattern,int context,ElemNumber namespaceContext) throws javax.xml.transform.TransformerException {
  DTM dtm=xctxt.getDTM(context);
  while (DTM.NULL != context) {
    if (null != fromMatchPattern) {
      if (fromMatchPattern.getMatchScore(xctxt,context) != XPath.MATCH_SCORE_NONE) {
        break;
      }
    }
    if (null != countMatchPattern) {
      if (countMatchPattern.getMatchScore(xctxt,context) != XPath.MATCH_SCORE_NONE) {
        break;
      }
    }
    context=dtm.getParent(context);
  }
  return context;
}
```
Original comment:
```
Given a \'from\' pattern (ala xsl:number), a match pattern and a context, find the first ancestor that matches the pattern (including the context handed in).
```
Generated comment:
```
Searches for the first occurence of the given argument, beginning the search at index, and testing for equality using the equals method.
```
---
id139
Code snippet:
```
@Deprecated protected void removeListeners(){
  if (propertyChangeListener != null) {
    comboBox.removePropertyChangeListener(propertyChangeListener);
  }
}
```
Original comment:
```
As of Java 2 platform v1.4 this method is no longer used.
```
Generated comment:
```
Removes the listener.
```
---
id140
Code snippet:
```
private void removeWaiter(WaitNode node){
  if (node != null) {
    node.thread=null;
    retry:     for (; ; ) {
      for (WaitNode pred=null, q=waiters, s; q != null; q=s) {
        s=q.next;
        if (q.thread != null)         pred=q;
 else         if (pred != null) {
          pred.next=s;
          if (pred.thread == null)           continue retry;
        }
 else         if (!UNSAFE.compareAndSwapObject(this,waitersOffset,q,s))         continue retry;
      }
      break;
    }
  }
}
```
Original comment:
```
Tries to unlink a timed-out or interrupted wait node to avoid accumulating garbage.  Internal nodes are simply unspliced without CAS since it is harmless if they are traversed anyway by releasers.  To avoid effects of unsplicing from already removed nodes, the list is retraversed in case of an apparent race.  This is slow when there are a lot of nodes, but we don\'t expect lists to be long enough to outweigh higher-overhead schemes.
```
Generated comment:
```
Removes and signals threads from queue for phase.
```
---
id141
Code snippet:
```
public Locator2Impl(){
}
```
Original comment:
```
Construct a new, empty Locator2Impl object. This will not normally be useful, since the main purpose of this class is to make a snapshot of an existing Locator.
```
Generated comment:
```
Creates a new instance.
```
---
id142
Code snippet:
```
public static AdjustmentListener add(AdjustmentListener a,AdjustmentListener b){
  return (AdjustmentListener)addInternal(a,b);
}
```
Original comment:
```
Adds adjustment-listener-a with adjustment-listener-b and returns the resulting multicast listener.
```
Generated comment:
```
Add a new listener.
```
---
id143
Code snippet:
```
public static void writeLines(Collection<?> lines,String lineEnding,OutputStream output) throws IOException {
  writeLines(lines,lineEnding,output,Charset.defaultCharset());
}
```
Original comment:
```
Writes the <code>toString()</code> value of each item in a collection to an <code>OutputStream</code> line by line, using the default character encoding of the platform and the specified line ending.
```
Generated comment:
```
Writes the <code>tostring()</code> value of each item in a collection to an <code>outputstream</code> line by line, using the specified character encoding and the specified line ending.
```
---
id144
Code snippet:
```
public void handleBtnRealmRequest(RequestInvocationEvent event){
  submitCycle=true;
  bRealmSelect=true;
  forwardTo();
}
```
Original comment:
```
Refreshes the view so that search for services can be done.
```
Generated comment:
```
Handles a request to the server.
```
---
id145
Code snippet:
```
public void doubleBufferingChanged(JRootPane rootPane){
}
```
Original comment:
```
Invoked when the doubleBuffered or useTrueDoubleBuffering properties of a JRootPane change.  This may come in on any thread.
```
Generated comment:
```
This method is called when a new frame is created.
```
---
id146
Code snippet:
```
public static void displayWarningDialog(Component parentComponent,LocalizableMessage title,LocalizableMessage msg){
  String plainText=msg.toString().replaceAll(\"<br>\",ServerConstants.EOL);
  String wrappedText=wrapText(plainText,70);
  wrappedText=wrappedText.replaceAll(ServerConstants.EOL,\"<br>\");
  JOptionPane.showMessageDialog(parentComponent,\"<html>\" + wrappedText,title.toString(),JOptionPane.WARNING_MESSAGE);
}
```
Original comment:
```
Displays a warning dialog.
```
Generated comment:
```
Displays a message to the user.
```
---
id147
Code snippet:
```
@Override public int hashCode(){
  int hash=LangUtils.HASH_SEED;
  hash=LangUtils.hashCode(hash,this.defaultPort);
  hash=LangUtils.hashCode(hash,this.name);
  hash=LangUtils.hashCode(hash,this.layered);
  hash=LangUtils.hashCode(hash,this.socketFactory);
  return hash;
}
```
Original comment:
```
Obtains a hash code for this scheme.
```
Generated comment:
```
Returns a hash code for this object.
```
---
id148
Code snippet:
```
public static final boolean isRectangleContainingRectangle(Rectangle a,Rectangle b){
  return b.x >= a.x && (b.x + b.width) <= (a.x + a.width) && b.y >= a.y && (b.y + b.height) <= (a.y + a.height);
}
```
Original comment:
```
Return true if <code>a</code> contains <code>b</code>
```
Generated comment:
```
Returns true if the specified rectangle is inside the rectangle of this rectangle.
```
---
id149
Code snippet:
```
static ComputedDayOfField ofWeekOfYearField(WeekFields weekDef){
  return new ComputedDayOfField(\"WeekOfYear\",weekDef,WEEKS,YEARS,WEEK_OF_YEAR_RANGE);
}
```
Original comment:
```
Returns a field to access the week of year, computed based on a WeekFields.
```
Generated comment:
```
Constructs a <code>years</code> representing the number of whole weeks in the specified year. <p> this factory method allows you to obtain a <code>yearmonthday</code> that may be immutable and unaffected by this method call.
```
---
id150
Code snippet:
```
@Override protected void onResume(){
  super.onResume();
  syncUIControlState();
}
```
Original comment:
```
Android Activity class methods
```
Generated comment:
```
Called when the activity is first created.
```
---
id151
Code snippet:
```
public Set createEntity(String entityName,String entityType,Map attributes) throws EntityException, SSOException {
  try {
    Object[] objs={tokenString,entityName,entityType,entityLocation,attributes};
    return ((Set)client.send(client.encodeMessage(\"createEntity\",objs),sessionCookies.getLBCookie(token.getTokenID().toString()),null));
  }
 catch (  RemoteException rex) {
    EntityUtils.debug.warning(\"EntityObject:createEntity->RemoteException\",rex);
    throw new EntityException(rex.getMessage(),\"1000\");
  }
catch (  Exception ex) {
    EntityUtils.debug.warning(\"EntityObject:createEntity->Exception\",ex);
    throw new EntityException(ex.getMessage(),\"1000\");
  }
}
```
Original comment:
```
Creates entity.
```
Generated comment:
```
Create an entity.
```
---
id152
Code snippet:
```
public void paint(GlyphView v,Graphics g,Shape a,int p0,int p1){
  sync(v);
  Segment text;
  TabExpander expander=v.getTabExpander();
  Rectangle alloc=(a instanceof Rectangle) ? (Rectangle)a : a.getBounds();
  int x=alloc.x;
  int p=v.getStartOffset();
  int[] justificationData=getJustificationData(v);
  if (p != p0) {
    text=v.getText(p,p0);
    int width=Utilities.getTabbedTextWidth(v,text,metrics,x,expander,p,justificationData);
    x+=width;
    SegmentCache.releaseSharedSegment(text);
  }
  int y=alloc.y + metrics.getHeight() - metrics.getDescent();
  text=v.getText(p0,p1);
  g.setFont(metrics.getFont());
  Utilities.drawTabbedText(v,text,x,y,g,expander,p0,justificationData);
  SegmentCache.releaseSharedSegment(text);
}
```
Original comment:
```
Paints the glyphs representing the given range.
```
Generated comment:
```
Paints the transcoded svg image on the specified graphics context. you can install a custom transformation on the graphics context to scale the image.
```
---
id153
Code snippet:
```
@Override protected void service(HttpServletRequest req,HttpServletResponse resp) throws ServletException, IOException {
  final String path=getRelativePath(req);
  if (isSpecialPath(path)) {
    resp.sendError(WebdavStatus.SC_NOT_FOUND);
    return;
  }
  final String method=req.getMethod();
  if (debug > 0) {
    log(\"[\" + method + \"] \"+ path);
  }
  if (method.equals(METHOD_PROPFIND)) {
    doPropfind(req,resp);
  }
 else   if (method.equals(METHOD_PROPPATCH)) {
    doProppatch(req,resp);
  }
 else   if (method.equals(METHOD_MKCOL)) {
    doMkcol(req,resp);
  }
 else   if (method.equals(METHOD_COPY)) {
    doCopy(req,resp);
  }
 else   if (method.equals(METHOD_MOVE)) {
    doMove(req,resp);
  }
 else   if (method.equals(METHOD_LOCK)) {
    doLock(req,resp);
  }
 else   if (method.equals(METHOD_UNLOCK)) {
    doUnlock(req,resp);
  }
 else {
    super.service(req,resp);
  }
}
```
Original comment:
```
Handles the special WebDAV methods.
```
Generated comment:
```
Perform an \"svn remove\" based on the request.
```
---
id154
Code snippet:
```
public PdfWin(PdfString f,PdfString d,PdfString o,PdfString p){
  this(new PdfDictionary());
  getPdfObject().put(PdfName.F,f);
  getPdfObject().put(PdfName.D,d);
  getPdfObject().put(PdfName.O,o);
  getPdfObject().put(PdfName.P,p);
}
```
Original comment:
```
Creates a new wrapper around a newly created Windows launch parameter dictionary.
```
Generated comment:
```
Creates a new instance.
```
---
id155
Code snippet:
```
protected void tearDown(){
}
```
Original comment:
```
Tears down the fixture, for example, close a network connection. This method is called after a test is executed.
```
Generated comment:
```
Tears down the fixture, for example, close a network connection. this method is called after a test is executed.
```
---
id156
Code snippet:
```
Object processNUMBER(StylesheetHandler handler,String uri,String name,String rawName,String value,ElemTemplateElement owner) throws org.xml.sax.SAXException {
  if (getSupportsAVT()) {
    Double val;
    AVT avt=null;
    try {
      avt=new AVT(handler,uri,name,rawName,value,owner);
      if (avt.isSimple()) {
        val=Double.valueOf(value);
      }
    }
 catch (    TransformerException te) {
      throw new org.xml.sax.SAXException(te);
    }
catch (    NumberFormatException nfe) {
      handleError(handler,XSLTErrorResources.INVALID_NUMBER,new Object[]{name,value},nfe);
      return null;
    }
    return avt;
  }
 else {
    try {
      return Double.valueOf(value);
    }
 catch (    NumberFormatException nfe) {
      handleError(handler,XSLTErrorResources.INVALID_NUMBER,new Object[]{name,value},nfe);
      return null;
    }
  }
}
```
Original comment:
```
Process an attribute string of type T_NUMBER into a double value.
```
Generated comment:
```
Process an attribute string of type t_int into a string value.
```
---
id157
Code snippet:
```
public void startRetransmitTimer(SIPServerTransaction sipServerTx,Response response){
  if (logger.isLoggingEnabled(LogWriter.TRACE_DEBUG)) {
    logger.logDebug(\"startRetransmitTimer() \" + response.getStatusCode() + \" method \"+ sipServerTx.getMethod());
  }
  if (sipServerTx.isInviteTransaction() && response.getStatusCode() / 100 == 2) {
    this.startTimer(sipServerTx);
  }
}
```
Original comment:
```
Start the retransmit timer.
```
Generated comment:
```
Start a transaction.
```
---
id158
Code snippet:
```
protected void fireEndDoc() throws org.xml.sax.SAXException {
  if (m_tracer != null) {
    flushMyWriter();
    m_tracer.fireGenerateEvent(SerializerTrace.EVENTTYPE_ENDDOCUMENT);
  }
}
```
Original comment:
```
To fire off end document trace event
```
Generated comment:
```
To fire off the document.
```
---
id159
Code snippet:
```
public com.sun.identity.saml2.jaxb.assertion.OneTimeUseElement createOneTimeUseElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.saml2.jaxb.assertion.impl.OneTimeUseElementImpl();
}
```
Original comment:
```
Create an instance of OneTimeUseElement
```
Generated comment:
```
Returns a new element for the given element.
```
---
id160
Code snippet:
```
public void handleBtnFilterRequest(RequestInvocationEvent event){
  CCDropDownMenu menu=(CCDropDownMenu)getChild(FILTER_TYPE);
  setPageSessionAttribute(ENTITY_TYPE,(String)menu.getValue());
  bFilter=true;
  submitCycle=true;
  forwardTo();
}
```
Original comment:
```
Handles filter results request.
```
Generated comment:
```
Handles a menu item.
```
---
id161
Code snippet:
```
public final void put(String key,int value){
  if ((m_firstFree + 1) >= m_mapSize) {
    m_mapSize+=m_blocksize;
    String newMap[]=new String[m_mapSize];
    System.arraycopy(m_map,0,newMap,0,m_firstFree + 1);
    m_map=newMap;
    int newValues[]=new int[m_mapSize];
    System.arraycopy(m_values,0,newValues,0,m_firstFree + 1);
    m_values=newValues;
  }
  m_map[m_firstFree]=key;
  m_values[m_firstFree]=value;
  m_firstFree++;
}
```
Original comment:
```
Append a string onto the vector.
```
Generated comment:
```
Inserts a key/value pair into the map.
```
---
id162
Code snippet:
```
public final void init(KeyStore ks,char[] password) throws KeyStoreException, NoSuchAlgorithmException, UnrecoverableKeyException {
  spiImpl.engineInit(ks,password);
}
```
Original comment:
```
Initializes this instance with the specified key store and password.
```
Generated comment:
```
Initialise the rsa engine.
```
---
id163
Code snippet:
```
public Folder(Context context,AttributeSet attrs){
  super(context,attrs);
  setAlwaysDrawnWithCacheEnabled(false);
  mInputMethodManager=(InputMethodManager)getContext().getSystemService(Context.INPUT_METHOD_SERVICE);
  Resources res=getResources();
  mExpandDuration=res.getInteger(R.integer.config_folderExpandDuration);
  mMaterialExpandDuration=res.getInteger(R.integer.config_materialFolderExpandDuration);
  mMaterialExpandStagger=res.getInteger(R.integer.config_materialFolderExpandStagger);
  if (sDefaultFolderName == null) {
    sDefaultFolderName=res.getString(R.string.folder_name);
  }
  if (sHintText == null) {
    sHintText=res.getString(R.string.folder_hint_text);
  }
  mLauncher=(Launcher)context;
  setFocusableInTouchMode(true);
}
```
Original comment:
```
Used to inflate the Workspace from XML.
```
Generated comment:
```
Creates a new instance.
```
---
id164
Code snippet:
```
protected void _skip7BitBinary() throws IOException {
  int origBytes=_readUnsignedVInt();
  int chunks=origBytes / 7;
  int encBytes=chunks * 8;
  origBytes-=7 * chunks;
  if (origBytes > 0) {
    encBytes+=1 + origBytes;
  }
  _skipBytes(encBytes);
}
```
Original comment:
```
Helper method for skipping length-prefixed binary data section
```
Generated comment:
```
Skips the specified number of bytes.
```
---
id165
Code snippet:
```
public static String byteArrayToHexString(byte[] byteArray){
  int readBytes=byteArray.length;
  StringBuffer hexData=new StringBuffer();
  int onebyte;
  for (int i=0; i < readBytes; i++) {
    onebyte=((0x000000ff & byteArray[i]) | 0xffffff00);
    hexData.append(Integer.toHexString(onebyte).substring(6));
  }
  return hexData.toString();
}
```
Original comment:
```
Converts a byte array to a hex string.
```
Generated comment:
```
Converts a byte array to a hexadecimal string.
```
---
id166
Code snippet:
```
public PWResetException(Throwable t){
  super(t);
  errList=new ArrayList(1);
  errList.add(t.getMessage());
}
```
Original comment:
```
Creates a password reset Exception object.
```
Generated comment:
```
Constructs a new instance with the given cause.
```
---
id167
Code snippet:
```
private static String parseStringValue(String parseString,String openTag,String closeTag,DataTypeValidationException exception) throws DataTypeValidationException {
  String tagValue;
  tagValue=parseTagValue(parseString,openTag,closeTag);
  if (tagValue == null) {
    throw exception;
  }
  return tagValue;
}
```
Original comment:
```
Parses out text located between first occurrences of the open and closed tags.
```
Generated comment:
```
Parses an nbt tag.
```
---
id168
Code snippet:
```
public AMSearchResults searchGroups(String wildcard,Map avPairs,AMSearchControl searchControl) throws AMException, SSOException {
  String filter=\"(|\" + getSearchFilter(AMObject.GROUP) + getSearchFilter(AMObject.DYNAMIC_GROUP)+ getSearchFilter(AMObject.ASSIGNABLE_DYNAMIC_GROUP)+ \")\";
  return searchObjects(AMNamingAttrManager.getNamingAttr(GROUP),filter,wildcard,avPairs,searchControl);
}
```
Original comment:
```
Searches for groups in this group using wildcards and attribute values. Wildcards can be specified such as a*, *, *a.
```
Generated comment:
```
Returns a query that matches the given criteria.
```
---
id169
Code snippet:
```
protected Tag(String id,boolean causesBreak,boolean isBlock){
  name=id;
  this.breakTag=causesBreak;
  this.blockTag=isBlock;
}
```
Original comment:
```
Creates a new <code>Tag</code> with the specified <code>id</code>; <code>causesBreak</code> and <code>isBlock</code> are defined by the user.
```
Generated comment:
```
Creates a new block.
```
---
id170
Code snippet:
```
public void configChanged(ConfigurationActionEvent e){
  if (Utils.debug.messageEnabled()) {
    Utils.debug.message(\"Utils.configChanged\");
  }
  setValues();
}
```
Original comment:
```
This method will be invoked when a component\'s  configuration data has been changed. The parameters componentName, realm and configName denotes the component name, organization and configuration instance name that are changed  respectively.
```
Generated comment:
```
This method gets called when a message is changed.
```
---
id171
Code snippet:
```
protected void addImpl(Component x,Object constraints,int index){
  if (x.getParent() == this) {
    return;
  }
 else {
    super.addImpl(x,constraints,index);
  }
}
```
Original comment:
```
If the specified component is already a child of this then we don\'t bother doing anything - stacking order doesn\'t matter for cell renderer components (CellRendererPane doesn\'t paint anyway).
```
Generated comment:
```
Add a constraint to the list.
```
---
id172
Code snippet:
```
public static boolean isValidIPv4(String address){
  if (address.length() == 0) {
    return false;
  }
  int octet;
  int octets=0;
  String temp=address + \".\";
  int pos;
  int start=0;
  while (start < temp.length() && (pos=temp.indexOf(\'.\',start)) > start) {
    if (octets == 4) {
      return false;
    }
    try {
      octet=Integer.parseInt(temp.substring(start,pos));
    }
 catch (    NumberFormatException ex) {
      return false;
    }
    if (octet < 0 || octet > 255) {
      return false;
    }
    start=pos + 1;
    octets++;
  }
  return octets == 4;
}
```
Original comment:
```
Validate the given IPv4 address.
```
Generated comment:
```
Validate the given ipv4 address.
```
---
id173
Code snippet:
```
public String toString(){
  String initState=\"\";
switch (state) {
case UNINITIALIZED:
    initState=\"<not initialized>\";
  break;
case VERIFY:
initState=\"<initialized for verifying>\";
break;
case SIGN:
initState=\"<initialized for signing>\";
break;
}
return \"Signature object: \" + getAlgorithm() + initState;
}
```
Original comment:
```
Returns a string representation of this signature object, providing information that includes the state of the object and the name of the algorithm used.
```
Generated comment:
```
Returns a string representation of this object.
```
---
id174
Code snippet:
```
public Boolean isAutoStopFileSizeEnabled(){
  return autoStopFileSizeEnable;
}
```
Original comment:
```
is auto stop file size enable
```
Generated comment:
```
Ruft den wert der enabled-eigenschaft ab.
```
---
id175
Code snippet:
```
private void safeDamageRange(int a0,int a1) throws BadLocationException {
  Document doc=component.getDocument();
  safeDamageRange(doc.createPosition(a0),doc.createPosition(a1));
}
```
Original comment:
```
Queues damageRange() call into event dispatch thread to be sure that views are in consistent state.
```
Generated comment:
```
Creates a new <code>document</code> object.
```
---
id176
Code snippet:
```
protected void runSQL(String sql){
  try {
    DataSource dataSource=fooPersistence.getDataSource();
    DB db=DBManagerUtil.getDB();
    sql=db.buildSQL(sql);
    sql=PortalUtil.transformSQL(sql);
    SqlUpdate sqlUpdate=SqlUpdateFactoryUtil.getSqlUpdate(dataSource,sql);
    sqlUpdate.update();
  }
 catch (  Exception e) {
    throw new SystemException(e);
  }
}
```
Original comment:
```
Performs a SQL query.
```
Generated comment:
```
Run the bigquery.
```
---
id177
Code snippet:
```
public String encode(){
  return encode(new StringBuilder()).toString();
}
```
Original comment:
```
Encode the user information as a string.
```
Generated comment:
```
Returns a string representation of this object.
```
---
id178
Code snippet:
```
public void push(final float value){
  int bits=Float.floatToIntBits(value);
  if (bits == 0L || bits == 0x3f800000 || bits == 0x40000000) {
    mv.visitInsn(Opcodes.FCONST_0 + (int)value);
  }
 else {
    mv.visitLdcInsn(value);
  }
}
```
Original comment:
```
Generates the instruction to push the given value on the stack.
```
Generated comment:
```
Generates the instruction to push the given value on the stack.
```
---
id179
Code snippet:
```
public void processBye(RequestEvent requestEvent,ServerTransaction serverTransactionId){
  SipProvider sipProvider=(SipProvider)requestEvent.getSource();
  Request request=requestEvent.getRequest();
  Dialog dialog=requestEvent.getDialog();
  System.out.println(\"local party = \" + dialog.getLocalParty());
  try {
    System.out.println(\"shootme:  got a bye sending OK.\");
    Response response=messageFactory.createResponse(200,request);
    serverTransactionId.sendResponse(response);
    System.out.println(\"Dialog State is \" + serverTransactionId.getDialog().getState());
  }
 catch (  Exception ex) {
    ex.printStackTrace();
    System.exit(0);
  }
}
```
Original comment:
```
Process the bye request.
```
Generated comment:
```
Processes a response.
```
---
id180
Code snippet:
```
public SAXException(String message,Exception e){
  super(message);
  this.exception=e;
}
```
Original comment:
```
Create a new SAXException from an existing exception. <p>The existing exception will be embedded in the new one, but the new exception will have its own message.</p>
```
Generated comment:
```
Constructs a new exception with the specified detail message. the cause is not initialized.
```
---
id181
Code snippet:
```
public void print(int i){
  writer.print(i);
}
```
Original comment:
```
Prints the given int.
```
Generated comment:
```
Description of the method.
```
---
id182
Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(characterdatasubstringexceedsvalue.class,args);
}
```
Original comment:
```
Runs this test from the command line.
```
Generated comment:
```
Runs this test from the command line.
```
---
id183
Code snippet:
```
public void start_scope(LogfileScope p_logfile_scope,boolean p_boolean_value){
  start_scope(p_logfile_scope);
  int int_value;
  if (p_boolean_value) {
    int_value=1;
  }
 else {
    int_value=0;
  }
  add_int(int_value);
}
```
Original comment:
```
Marks the beginning of a new scope in the output stream Writes also 1, if p_boolean_value is true, or 0, if p_boolean_value is false;
```
Generated comment:
```
Start a new log file.
```
---
id184
Code snippet:
```
public final int hashCode(){
  if (toString() == null) {
    return 0;
  }
  return toString().hashCode();
}
```
Original comment:
```
Finalizes the hashCode method
```
Generated comment:
```
Returns a hash code for this instance.
```
---
id185
Code snippet:
```
public GeneralName(int tag,ASN1Encodable name){
  this.obj=name;
  this.tag=tag;
}
```
Original comment:
```
When the subjectAltName extension contains an Internet mail address, the address MUST be included as an rfc822Name. The format of an rfc822Name is an \"addr-spec\" as defined in RFC 822 [RFC 822]. When the subjectAltName extension contains a domain name service label, the domain name MUST be stored in the dNSName (an IA5String). The name MUST be in the \"preferred name syntax,\" as specified by RFC 1034 [RFC 1034]. When the subjectAltName extension contains a URI, the name MUST be stored in the uniformResourceIdentifier (an IA5String). The name MUST be a non-relative URL, and MUST follow the URL syntax and encoding rules specified in [RFC 1738].  The name must include both a scheme (e.g., \"http\" or \"ftp\") and a scheme-specific-part.  The scheme- specific-part must include a fully qualified domain name or IP address as the host. When the subjectAltName extension contains a iPAddress, the address MUST be stored in the octet string in \"network byte order,\" as specified in RFC 791 [RFC 791]. The least significant bit (LSB) of each octet is the LSB of the corresponding byte in the network address. For IP Version 4, as specified in RFC 791, the octet string MUST contain exactly four octets.  For IP Version 6, as specified in RFC 1883, the octet string MUST contain exactly sixteen octets [RFC 1883].
```
Generated comment:
```
Creates a new instance of derexternal. see x.690 for more informations about the meaning of these parameters.
```
---
id186
Code snippet:
```
public MalformedURLException(String detailMessage,Throwable cause){
  super(detailMessage,cause);
}
```
Original comment:
```
Constructs a new instance with given detail message and cause.
```
Generated comment:
```
Constructs a new instance with the given detail message and cause.
```
---
id187
Code snippet:
```
public Response[] send(Member[] destination,Serializable message,int rpcOptions,int channelOptions,long timeout) throws ChannelException {
  if (destination == null || destination.length == 0)   return new Response[0];
  int sendOptions=channelOptions & ~Channel.SEND_OPTIONS_SYNCHRONIZED_ACK;
  RpcCollectorKey key=new RpcCollectorKey(UUIDGenerator.randomUUID(false));
  RpcCollector collector=new RpcCollector(key,rpcOptions,destination.length);
  try {
synchronized (collector) {
      if (rpcOptions != NO_REPLY)       responseMap.put(key,collector);
      RpcMessage rmsg=new RpcMessage(rpcId,key.id,message);
      channel.send(destination,rmsg,sendOptions);
      if (rpcOptions != NO_REPLY)       collector.wait(timeout);
    }
  }
 catch (  InterruptedException ix) {
    Thread.currentThread().interrupt();
  }
 finally {
    responseMap.remove(key);
  }
  return collector.getResponses();
}
```
Original comment:
```
Send a message and wait for the response.
```
Generated comment:
```
Sends a message to the recipient.
```
---
id188
Code snippet:
```
@SuppressWarnings(\"unused\") public void openFileChooser(ValueCallback<Uri> uploadMsg,String acceptType,String capture){
  openFileChooser(uploadMsg,acceptType);
}
```
Original comment:
```
may not work on KitKat due to lack of implementation of openFileChooser() or onShowFileChooser() https://code.google.com/p/android/issues/detail?id=62220 however newer versions of KitKat fixed it on some devices
```
Generated comment:
```
Opens the specified url.
```
---
id189
Code snippet:
```
protected void tearDown(){
  Locale.setDefault(defaultLocale);
}
```
Original comment:
```
Tears down the fixture, for example, close a network connection. This method is called after a test is executed.
```
Generated comment:
```
Tears down the fixture, for example, close a network connection. this method is called after a test is executed.
```
---
id190
Code snippet:
```
public static ComponentUI createUI(JComponent a){
  ComponentUI mui=new MultiColorChooserUI();
  return MultiLookAndFeel.createUIs(mui,((MultiColorChooserUI)mui).uis,a);
}
```
Original comment:
```
Returns a multiplexing UI instance if any of the auxiliary <code>LookAndFeel</code>s supports this UI.  Otherwise, just returns the UI object obtained from the default <code>LookAndFeel</code>.
```
Generated comment:
```
Returns a multiplexing ui instance if any of the auxiliary <code>lookandfeel</code>s supports this ui. otherwise, just returns the ui object obtained from the default <code>lookandfeel</code>.
```
---
id191
Code snippet:
```
private ByteString(final byte[] b,final int offset,final int length){
  this.buffer=b;
  this.offset=offset;
  this.length=length;
}
```
Original comment:
```
Creates a new byte string that wraps a subsequence of the provided byte array. <p> <b>NOTE:</b> this method takes ownership of the provided byte array and, therefore, the byte array MUST NOT be altered directly after this method returns.
```
Generated comment:
```
Creates a new byte array.
```
---
id192
Code snippet:
```
static String readQuotedString(final SubstringReader reader) throws DecodeException {
  int length=0;
  reader.skipWhitespaces();
  try {
    final char c=reader.read();
    if (c != \'\\'\') {
      throw DecodeException.error(ERR_ATTR_SYNTAX_EXPECTED_QUOTE_AT_POS1.get(reader.pos() - 1,c));
    }
    reader.mark();
    while (reader.read() != \'\\'\') {
      length++;
    }
    reader.reset();
    final String str=reader.read(length);
    reader.read();
    return str;
  }
 catch (  final StringIndexOutOfBoundsException e) {
    throw DecodeException.error(ERR_ATTR_SYNTAX_TRUNCATED_VALUE1.get());
  }
}
```
Original comment:
```
Reads the value of a string enclosed in single quotes, skipping over the quotes and any leading spaces.
```
Generated comment:
```
Returns the remainder of \'reader\' as a string, closing it when done.
```
---
id193
Code snippet:
```
public ECPrivateKeySpec(BigInteger s,ECParameterSpec params){
  if (s == null) {
    throw new NullPointerException(\"s is null\");
  }
  if (params == null) {
    throw new NullPointerException(\"params is null\");
  }
  this.s=s;
  this.params=params;
}
```
Original comment:
```
Creates a new ECPrivateKeySpec with the specified parameter values.
```
Generated comment:
```
Creates a new <code>dhparameterspec</code> instance with the specified parameters.
```
---
id194
Code snippet:
```
public void skippedEntity(String name) throws SAXException {
  flushStartDoc();
  m_resultContentHandler.skippedEntity(name);
}
```
Original comment:
```
Receive notification of a skipped entity. <p>By default, do nothing.  Application writers may override this method in a subclass to take specific actions for each processing instruction, such as setting status variables or invoking other methods.</p>
```
Generated comment:
```
Receive notification of a skipped entity. <p>by default, do nothing. application writers may override this method in a subclass to take specific actions for each processing instruction, such as setting status variables or invoking other methods.</p>.
```
---
id195
Code snippet:
```
public EntryChangeNotificationControl(boolean isCritical,PersistentSearchChangeType changeType,long changeNumber){
  super(OID_ENTRY_CHANGE_NOTIFICATION,isCritical);
  this.changeType=changeType;
  this.changeNumber=changeNumber;
  previousDN=null;
}
```
Original comment:
```
Creates a new entry change notification control with the provided information.
```
Generated comment:
```
Creates a new notification object.
```
---
id196
Code snippet:
```
private ConcurrentSkipListMap.Node<K,V> loNode(){
  if (lo == null)   return m.findFirst();
 else   if (loInclusive)   return m.findNear(lo,GT | EQ);
 else   return m.findNear(lo,GT);
}
```
Original comment:
```
Returns lowest node. This node might not be in range, so most usages need to check bounds.
```
Generated comment:
```
Returns highest node. this node might not be in range, so most usages need to check bounds.
```
---
id197
Code snippet:
```
public void testCertificateFactory06() throws CertificateException {
  if (!X509Support) {
    fail(NotSupportMsg);
    return;
  }
  Provider provider=null;
  for (int i=0; i < validValues.length; i++) {
    try {
      CertificateFactory.getInstance(validValues[i],provider);
      fail(\"IllegalArgumentException must be thrown  when provider is null\");
    }
 catch (    IllegalArgumentException e) {
    }
  }
}
```
Original comment:
```
Test for <code>getInstance(String type, Provider provider)</code> method Assertion: throws IllegalArgumentException when provider is null
```
Generated comment:
```
Test for <code>getinstance(string type, string provider)</code> method assertion: throws nullpointerexception when type is null.
```
---
id198
Code snippet:
```
protected static boolean networkMonitorExist(String nwMonName){
  String classMethod=\"OpenSSOMonitoringUtil.networkMonitorExist: \";
  if (debug.messageEnabled()) {
    debug.message(classMethod + \"checking \" + nwMonName);
  }
  if ((nwMonName == null) || (nwMonName.length() == 0)) {
    if (debug.warningEnabled()) {
      debug.warning(classMethod + \"isNull\");
    }
    return false;
  }
  Set<String> ntwStats=NetworkMonitor.getInstanceNames();
  String ss=nwMonName.toLowerCase();
  if (ntwStats.contains(ss)) {
    return true;
  }
 else {
    return false;
  }
}
```
Original comment:
```
return whether the specified network monitor has been instantiated in the entitlements service yet
```
Generated comment:
```
Returns true if the given element is a valid class.
```
---
id199
Code snippet:
```
private void handleError(final ConnectorException e,final IConfiguration configuration,final HttpServletRequest request,final HttpServletResponse response,final String currentCommand) throws ServletException {
  try {
    if (currentCommand != null) {
      Command command=CommandHandlerEnum.valueOf(currentCommand.toUpperCase()).getCommand();
      if (command instanceof XMLCommand) {
        CommandHandlerEnum.XMLERROR.execute(request,response,configuration,getServletContext(),e);
      }
 else {
        CommandHandlerEnum.ERROR.execute(request,response,configuration,getServletContext(),e);
      }
    }
 else {
      CommandHandlerEnum.XMLERROR.execute(request,response,configuration,getServletContext(),e);
    }
  }
 catch (  Exception e1) {
    throw new ServletException(e1);
  }
}
```
Original comment:
```
handles error from execute command.
```
Generated comment:
```
Handles the http <code>get</code> method.
```
---
id200
Code snippet:
```
public void visitAttribute(Attribute attr){
  if (fv != null) {
    fv.visitAttribute(attr);
  }
}
```
Original comment:
```
Visits a non standard attribute of the field.
```
Generated comment:
```
Visits a non standard attribute of the class.
```
---
id201
Code snippet:
```
@Override public boolean equals(Object obj){
  if (obj == null) {
    return false;
  }
  if (!getClass().equals(obj.getClass())) {
    return false;
  }
  StaticAttributes object=(StaticAttributes)obj;
  if (propertyName == null) {
    if (object.propertyName != null) {
      return false;
    }
  }
 else {
    if (!propertyName.equals(object.propertyName)) {
      return false;
    }
  }
  if (propertyValues == null) {
    if (object.propertyValues != null) {
      return false;
    }
  }
 else {
    if (!propertyValues.equals(object.propertyValues)) {
      return false;
    }
  }
  if (pResponseProviderName == null) {
    if (object.getPResponseProviderName() != null) {
      return false;
    }
  }
 else {
    if (!pResponseProviderName.equals(object.getPResponseProviderName())) {
      return false;
    }
  }
  return true;
}
```
Original comment:
```
Returns <code>true</code> if the passed in object is equal to this object
```
Generated comment:
```
Tests this instance for equality with an arbitrary object.
```
---
id202
Code snippet:
```
public void treeExpanded(TreeExpansionEvent event){
  getHandler().treeExpanded(event);
}
```
Original comment:
```
Called whenever an item in the tree has been expanded.
```
Generated comment:
```
This method is called when a node is removed from the tree.
```
---
id203
Code snippet:
```
public MidiFileFormat(int type,float divisionType,int resolution,int bytes,long microseconds){
  this.type=type;
  this.divisionType=divisionType;
  this.resolution=resolution;
  this.byteLength=bytes;
  this.microsecondLength=microseconds;
  this.properties=null;
}
```
Original comment:
```
Constructs a <code>MidiFileFormat</code>.
```
Generated comment:
```
Creates a new instance.
```
---
id204
Code snippet:
```
public void error(XPathContext xctxt,int sourceNode,String msg,Object[] args) throws javax.xml.transform.TransformerException {
  String fmsg=XSLMessages.createXPATHMessage(msg,args);
  ErrorListener ehandler=xctxt.getErrorListener();
  if (null != ehandler) {
    ehandler.fatalError(new TransformerException(fmsg,(SAXSourceLocator)xctxt.getSAXLocator()));
  }
 else {
    SourceLocator slocator=xctxt.getSAXLocator();
    System.out.println(fmsg + \"; file \" + slocator.getSystemId()+ \"; line \"+ slocator.getLineNumber()+ \"; column \"+ slocator.getColumnNumber());
  }
}
```
Original comment:
```
Tell the user of an error, and probably throw an exception.
```
Generated comment:
```
Tell the user of an error, and probably throw an exception.
```
---
id205
Code snippet:
```
private boolean verifyLogRecord(String[] record,int macPos) throws Exception {
  StringBuilder data=new StringBuilder();
  for (int m=0; m < record.length - 2; m++) {
    data.append(record[m]);
  }
  curMAC=record[macPos];
  verified=helper.verifyMAC(data.toString(),helper.toByteArray(curMAC));
  return verified;
}
```
Original comment:
```
Verifies the passed LogRecord to check for tampering.
```
Generated comment:
```
Verify that the message is valid.
```
---
id206
Code snippet:
```
@Override public Foo fetchByField2_First(boolean field2,OrderByComparator<Foo> orderByComparator){
  List<Foo> list=findByField2(field2,0,1,orderByComparator);
  if (!list.isEmpty()) {
    return list.get(0);
  }
  return null;
}
```
Original comment:
```
Returns the first foo in the ordered set where field2 = &#63;.
```
Generated comment:
```
Find the _fields constant that matches fieldid, or null if its not found.
```
---
id207
Code snippet:
```
public Builder names(final String... names){
  return names(asList(names));
}
```
Original comment:
```
Adds the provided user friendly names.
```
Generated comment:
```
Creates a new builder.
```
---
id208
Code snippet:
```
private String createRegistrationAccessToken(Client client,OAuth2Request request) throws ServerException, NotFoundException {
  final AccessToken rat=tokenStore.createAccessToken(null,OAuth2Constants.Bearer.BEARER,null,client.getClientID(),client.getClientID(),null,Collections.<String>emptySet(),null,null,null,request);
  return rat.getTokenId();
}
```
Original comment:
```
Creates a fresh registration access token for the case where open dynamic registration is enabled and the client has registered without providing an access token. This allows the client to use the client registration endpoint to manage their registration.
```
Generated comment:
```
Creates a new token.
```
---
id209
Code snippet:
```
public AMSearchResults searchDynamicGroups(String wildcard,AMSearchControl searchControl) throws AMException, SSOException {
  return searchDynamicGroups(wildcard,null,searchControl);
}
```
Original comment:
```
Searches for dynamic groups in this organization unit using wildcards. Wildcards can be specified such as a*, *, *a.
```
Generated comment:
```
Searches for a search result for the given search string.
```
---
id210
Code snippet:
```
protected static AttrSet combineAttrSets(AttrSet attrSet1,AttrSet attrSet2){
  AttrSet retAttrSet=new AttrSet();
  if (attrSet1 != null) {
    int count=attrSet1.size();
    for (int i=0; i < count; i++) {
      Attr attr=attrSet1.elementAt(i);
      retAttrSet.add(attr);
    }
  }
  if (attrSet2 != null) {
    int count=attrSet2.size();
    for (int i=0; i < count; i++) {
      Attr attr=attrSet2.elementAt(i);
      retAttrSet.add(attr);
    }
  }
  return retAttrSet;
}
```
Original comment:
```
Combines 2 AttrSets and returns the result set. The original sets are not modified.
```
Generated comment:
```
Combines a set of attributes with the given one.
```
---
id211
Code snippet:
```
public void logWarning(String string){
  getLogger().warn(string);
}
```
Original comment:
```
Log a warning mesasge.
```
Generated comment:
```
Log a message, specifying source class and method, with an array of object arguments. <p> if the logger is currently enabled for the given message level then the given message is forwarded to all the registered output handler objects. <p>.
```
---
id212
Code snippet:
```
public long executeForLong(String sql,Object[] bindArgs,int connectionFlags,CancellationSignal cancellationSignal){
  if (sql == null) {
    throw new IllegalArgumentException(\"sql must not be null.\");
  }
  if (executeSpecial(sql,bindArgs,connectionFlags,cancellationSignal)) {
    return 0;
  }
  acquireConnection(sql,connectionFlags,cancellationSignal);
  try {
    return mConnection.executeForLong(sql,bindArgs,cancellationSignal);
  }
  finally {
    releaseConnection();
  }
}
```
Original comment:
```
Executes a statement that returns a single <code>long</code> result.
```
Generated comment:
```
Execute a statement that returns a 1 by 1 table with the value passed as a parameter.
```
---
id213
Code snippet:
```
public void testIsConnected_WithServer() throws IOException {
  connectLocalServer();
  disconnectAfterConnected();
  this.datagramSocket1.close();
  this.channel1.close();
  assertFalse(this.channel1.isConnected());
}
```
Original comment:
```
Test method for \'DatagramChannelImpl.isConnected()\'
```
Generated comment:
```
Test method for \'datagramchannelimpl.connect(socketaddress)\'.
```
---
id214
Code snippet:
```
public void testClearBitZeroOutside1(){
  byte aBytes[]={0};
  int aSign=0;
  int number=95;
  byte rBytes[]={0};
  BigInteger aNumber=new BigInteger(aSign,aBytes);
  BigInteger result=aNumber.clearBit(number);
  byte resBytes[]=new byte[rBytes.length];
  resBytes=result.toByteArray();
  for (int i=0; i < resBytes.length; i++) {
    assertTrue(resBytes[i] == rBytes[i]);
  }
  assertEquals(\"incorrect sign\",0,result.signum());
}
```
Original comment:
```
clearBit(int n) outside zero
```
Generated comment:
```
Clearbit(int n) outside a negative number.
```
---
id215
Code snippet:
```
public void testGetKeyLength(){
  char[] password=new char[]{\'1\',\'2\',\'3\',\'4\',\'5\'};
  byte[] salt=new byte[]{1,2,3,4,5};
  int iterationCount=10;
  int keyLength=10;
  PBEKeySpec pbeks=new PBEKeySpec(password,salt,iterationCount,keyLength);
  assertTrue(\"The returned keyLength is not equal to the value specified \" + \"in the constructor.\",pbeks.getKeyLength() == keyLength);
  pbeks=new PBEKeySpec(password);
  assertTrue(\"The getKeyLength() method should return 0 \" + \"if the keyLength is not specified.\",pbeks.getKeyLength() == 0);
}
```
Original comment:
```
getKeyLength() method testing.
```
Generated comment:
```
Test for <code>getpasswordcount()</code> method.
```
---
id216
Code snippet:
```
public boolean hasUnsupportedCriticalExtension(){
  Set extns=getCriticalExtensionOIDs();
  return extns != null && !extns.isEmpty();
}
```
Original comment:
```
Will return true if any extensions are present and marked as critical as we currently don\'t handle any extensions!
```
Generated comment:
```
Returns whether it has the extension.
```
---
id217
Code snippet:
```
@Override public boolean isEmpty(){
  return size == 0;
}
```
Original comment:
```
Returns whether this map is empty.
```
Generated comment:
```
Returns <tt>true</tt> if this map contains no key-value mappings.
```
---
id218
Code snippet:
```
public void test_chooseServerAlias(){
  init(SERVER);
  assertNull(manager.chooseServerAlias(null,null,new Socket()));
  assertNull(manager.chooseServerAlias(\"\",null,new Socket()));
  String res=manager.chooseServerAlias(TYPE_RSA,null,null);
  assertNotNull(res);
  assertEquals(\"serverkey_00\",res.toLowerCase());
  res=manager.chooseServerAlias(TYPE_RSA,null,new Socket());
  assertNotNull(res);
  assertEquals(\"serverkey_00\",res.toLowerCase());
}
```
Original comment:
```
X509KeyManager#chooseServerAlias(String keyType, Principal[] issuers, Socket socket)
```
Generated comment:
```
Javax.net.ssl.sslsocket#sslsocket(java.net.net.ssl.sslsocket).
```
---
id219
Code snippet:
```
public java.util.List<HDR> subList(int index1,int index2){
  return this.hlist.subList(index1,index2);
}
```
Original comment:
```
Get a sublist of the list.
```
Generated comment:
```
Returns the index of the first occurrence of the specified element. returns <code>null</code> if the receiver does not contain this element. searches between <code>from</code>, inclusive and <code>to</code>, inclusive. tests for identity.
```
---
id220
Code snippet:
```
protected String long2roman(long val,boolean prefixesAreOK){
  if (val <= 0) {
    return getZeroString();
  }
  String roman=\"\";
  int place=0;
  if (val <= 3999L) {
    do {
      while (val >= m_romanConvertTable[place].m_postValue) {
        roman+=m_romanConvertTable[place].m_postLetter;
        val-=m_romanConvertTable[place].m_postValue;
      }
      if (prefixesAreOK) {
        if (val >= m_romanConvertTable[place].m_preValue) {
          roman+=m_romanConvertTable[place].m_preLetter;
          val-=m_romanConvertTable[place].m_preValue;
        }
      }
      place++;
    }
 while (val > 0);
  }
 else {
    roman=XSLTErrorResources.ERROR_STRING;
  }
  return roman;
}
```
Original comment:
```
Convert a long integer into roman numerals.
```
Generated comment:
```
Convert a long value to a long value.
```
---
id221
Code snippet:
```
public int new_no(){
  if (last_generated_id_no >= c_max_id_no) {
    System.err.println(\"IdGenerator: danger of overflow, please regenerate id numbers from scratch!\");
  }
  last_generated_id_no++;
  return last_generated_id_no;
}
```
Original comment:
```
Create a new unique identification number.
```
Generated comment:
```
Returns a random number from the distribution.
```
---
id222
Code snippet:
```
public boolean beginUnselectedChoiceDisplay(ChildDisplayEvent event){
  return (curTile != defaultValue);
}
```
Original comment:
```
begins display of unselected choice
```
Generated comment:
```
Returns <code>true</code> if <code>selection</code> is <code>true</code>.
```
---
id223
Code snippet:
```
public static String toUnicode(String input,int flag){
  int p=0, q=0;
  StringBuffer out=new StringBuffer();
  if (isRootLabel(input)) {
    return \".\";
  }
  while (p < input.length()) {
    q=searchDots(input,p);
    out.append(toUnicodeInternal(input.substring(p,q),flag));
    if (q != (input.length())) {
      out.append(\'.\');
    }
    p=q + 1;
  }
  return out.toString();
}
```
Original comment:
```
Translates a string from ASCII Compatible Encoding (ACE) to Unicode, as defined by the ToUnicode operation of <a href=\"http://www.ietf.org/rfc/rfc3490.txt\">RFC 3490</a>. <p>ToUnicode never fails. In case of any error, the input string is returned unmodified. <p> A label is an individual part of a domain name. The original ToUnicode operation, as defined in RFC 3490, only operates on a single label. This method can handle both label and entire domain name, by assuming that labels in a domain name are always separated by dots. The following characters are recognized as dots: &#0092;u002E (full stop), &#0092;u3002 (ideographic full stop), &#0092;uFF0E (fullwidth full stop), and &#0092;uFF61 (halfwidth ideographic full stop).
```
Generated comment:
```
Returns a string representation of this object.
```
---
id224
Code snippet:
```
static private byte[] toBytes(ASN1OctetString[] octs){
  ByteArrayOutputStream bOut=new ByteArrayOutputStream();
  for (int i=0; i != octs.length; i++) {
    try {
      DEROctetString o=(DEROctetString)octs[i];
      bOut.write(o.getOctets());
    }
 catch (    ClassCastException e) {
      throw new IllegalArgumentException(octs[i].getClass().getName() + \" found in input should only contain DEROctetString\");
    }
catch (    IOException e) {
      throw new IllegalArgumentException(\"exception converting octets \" + e.toString());
    }
  }
  return bOut.toByteArray();
}
```
Original comment:
```
convert a vector of octet strings into a single byte string
```
Generated comment:
```
Produce an object suitable for an asn1outputstream.
```
---
id225
Code snippet:
```
public int next(){
  _currentNode=(_currentNode == DTM.NULL) ? DTM.NULL : _nextsib(_currentNode);
  return returnNode(makeNodeHandle(_currentNode));
}
```
Original comment:
```
Get the next node in the iteration.
```
Generated comment:
```
Get the next node in the iteration.
```
---
id226
Code snippet:
```
public CharVector(char[] a){
  blockSize=DEFAULT_BLOCK_SIZE;
  array=a;
  n=a.length;
}
```
Original comment:
```
Construct char vector instance.
```
Generated comment:
```
Creates a new char array.
```
---
id227
Code snippet:
```
public void testHandleLowMemory() throws Exception {
  assertNull(cache.toVerboseString(),\"Expected empty cache.  \" + \"Cache contents:\" + ServerConstants.EOL + cache.toVerboseString());
  cache.handleLowMemory();
  cache.clear();
}
```
Original comment:
```
Tests the <CODE>handleLowMemory</CODE> method.
```
Generated comment:
```
Test memory cache.
```
---
id228
Code snippet:
```
public synchronized AttributeSet addAttribute(AttributeSet old,Object name,Object value){
  if ((old.getAttributeCount() + 1) <= getCompressionThreshold()) {
    search.removeAttributes(search);
    search.addAttributes(old);
    search.addAttribute(name,value);
    reclaim(old);
    return getImmutableUniqueSet();
  }
  MutableAttributeSet ma=getMutableAttributeSet(old);
  ma.addAttribute(name,value);
  return ma;
}
```
Original comment:
```
Adds an attribute to the given set, and returns the new representative set. <p> This method is thread safe, although most Swing methods are not. Please see <A HREF=\"https://docs.oracle.com/javase/tutorial/uiswing/concurrency/index.html\">Concurrency in Swing</A> for more information.
```
Generated comment:
```
Adds an attribute to the set.
```
---
id229
Code snippet:
```
public SIPHeader parse() throws ParseException {
  MinSE minse=new MinSE();
  if (debug)   dbg_enter(\"parse\");
  try {
    headerName(TokenTypes.MINSE_TO);
    String nextId=lexer.getNextId();
    try {
      int delta=Integer.parseInt(nextId);
      minse.setExpires(delta);
    }
 catch (    NumberFormatException ex) {
      throw createParseException(\"bad integer format\");
    }
catch (    InvalidArgumentException ex) {
      throw createParseException(ex.getMessage());
    }
    this.lexer.SPorHT();
    super.parse(minse);
    return minse;
  }
  finally {
    if (debug)     dbg_leave(\"parse\");
  }
}
```
Original comment:
```
Parse the header.
```
Generated comment:
```
Parse the string message.
```
---
id230
Code snippet:
```
public AttributeTable add(ASN1ObjectIdentifier attrType,ASN1Encodable attrValue){
  AttributeTable newTable=new AttributeTable(attributes);
  newTable.addAttribute(attrType,new Attribute(attrType,new DERSet(attrValue)));
  return newTable;
}
```
Original comment:
```
Return a new table with the passed in attribute added.
```
Generated comment:
```
Add an attribute to the set.
```
---
id231
Code snippet:
```
private final void releaseDTMXRTreeFrags(){
  if (m_DTMXRTreeFrags == null) {
    return;
  }
  final Iterator iter=(m_DTMXRTreeFrags.values()).iterator();
  while (iter.hasNext()) {
    DTMXRTreeFrag frag=(DTMXRTreeFrag)iter.next();
    frag.destruct();
    iter.remove();
  }
  m_DTMXRTreeFrags=null;
}
```
Original comment:
```
Cleans DTMXRTreeFrag objects by removing references  to DTM and XPathContext objects.
```
Generated comment:
```
Releases all references to it.
```
---
id232
Code snippet:
```
public SQLRecoverableException(){
}
```
Original comment:
```
Creates an SQLRecoverableException object. The Reason string is set to null, the SQLState string is set to null and the Error Code is set to 0.
```
Generated comment:
```
Creates an sqltransientexception object. the reason string is set to null, the sqlstate string is set to null and the error code is set to 0.
```
---
id233
Code snippet:
```
public void reclaim(AttributeSet a){
  if (SwingUtilities.isEventDispatchThread()) {
    attributesPool.size();
  }
}
```
Original comment:
```
Returns a set no longer needed by the MutableAttributeSet implementation. This is useful for operation under 1.1 where there are no weak references.  This would typically be called by the finalize method of the MutableAttributeSet implementation. <p> This method is thread safe, although most Swing methods are not. Please see <A HREF=\"https://docs.oracle.com/javase/tutorial/uiswing/concurrency/index.html\">Concurrency in Swing</A> for more information.
```
Generated comment:
```
Sets the attributes of this element.
```
---
id234
Code snippet:
```
private void readObject(java.io.ObjectInputStream stream) throws IOException, ClassNotFoundException {
  if (stubDelegate == null) {
    setDefaultDelegate();
  }
  if (stubDelegate != null) {
    stubDelegate.readObject(this,stream);
  }
}
```
Original comment:
```
Serialization method to restore the IOR state.
```
Generated comment:
```
Adds semantic checks to the default deserialization method. this method must have the standard signature for a readobject method, and the body of the method must begin with \"s.defaultreadobject();\". other than that, any semantic checks can be specified and do not need to stay the same from version to version. a readobject method of this form may be added to any class, even if tetrad sessions were previously saved out using a version of the class that didn\'t include it. (that\'s what the \"s.defaultreadobject();\" is for. see j. bloch, effective java, for help.
```
---
id235
Code snippet:
```
protected void copy(WebResource resource,InputStream is,PrintWriter writer,String encoding) throws IOException {
  IOException exception=null;
  InputStream resourceInputStream=null;
  if (resource.isFile()) {
    resourceInputStream=resource.getInputStream();
  }
 else {
    resourceInputStream=is;
  }
  Reader reader;
  if (encoding == null) {
    reader=new InputStreamReader(resourceInputStream);
  }
 else {
    reader=new InputStreamReader(resourceInputStream,encoding);
  }
  exception=copyRange(reader,writer);
  reader.close();
  if (exception != null)   throw exception;
}
```
Original comment:
```
Copy the contents of the specified input stream to the specified output stream, and ensure that both streams are closed before returning (even in the face of an exception).
```
Generated comment:
```
Copy a inputstream to a outputstream.
```
---
id236
Code snippet:
```
public static boolean checkStatement(Element element,String statementname){
  if (element == null || statementname == null) {
    return false;
  }
  String tag=element.getLocalName();
  if (tag == null) {
    return false;
  }
 else   if (tag.equals(\"Statement\")) {
    NamedNodeMap nm=element.getAttributes();
    int len=nm.getLength();
    String attrName=null;
    Attr attr=null;
    for (int j=0; j < len; j++) {
      attr=(Attr)nm.item(j);
      attrName=attr.getLocalName();
      if ((attrName != null) && (attrName.equals(\"type\")) && (attr.getNodeValue().equals(statementname + \"Type\"))) {
        return true;
      }
    }
  }
 else   if (tag.equals(statementname)) {
    return true;
  }
  return false;
}
```
Original comment:
```
Verifies if an element is a type of a specific statement. Currently, this method is used by class AuthnStatementImpl, AuthzDecisionStatement and AttributeStatementImpl.
```
Generated comment:
```
Checks whether the given element is a variable.
```
---
id237
Code snippet:
```
public boolean hasSalary(){
  return fieldSetFlags()[3];
}
```
Original comment:
```
Checks whether the \'salary\' field has been set.
```
Generated comment:
```
Returns whether it has the value.
```
---
id238
Code snippet:
```
public void addConnection(boolean success){
  if (success) {
    connectionMonitor.add();
  }
 else {
    failureConnectionMonitor.add();
  }
}
```
Original comment:
```
Increments the counter for a connection. Boolean indicator controls whether we increment the successful or unsuccessful connection counter.
```
Generated comment:
```
Adds a connection to the list of connections.
```
---
id239
Code snippet:
```
private boolean is(int flags){
  return (m_flags & flags) != 0;
}
```
Original comment:
```
Tell if this element type has the basic bit properties that are passed as an argument.
```
Generated comment:
```
Returns whether the given flags includes the given flags.
```
---
id240
Code snippet:
```
public static Map appendMapToMap(Map mapToAdd,Map toMap){
  if ((mapToAdd != null) && (toMap != null)) {
    Set keySet=mapToAdd.keySet();
    Iterator keyIter=keySet.iterator();
    while (keyIter.hasNext()) {
      String key=(String)keyIter.next();
      Set values=(Set)mapToAdd.get(key);
      appendElementToMap(key,values,toMap);
    }
  }
  return toMap;
}
```
Original comment:
```
Appends a map to another map
```
Generated comment:
```
Append a key-value pair to the map.
```
---
id241
Code snippet:
```
private void addFQDNDigestMD5() throws ConfigureDSException {
  try {
    updateConfigEntryWithAttribute(DN_DIGEST_MD5_SASL_MECHANISM,\"ds-cfg-server-fqdn\",CoreSchema.getDirectoryStringSyntax(),hostName.getValue());
  }
 catch (  final Exception e) {
    throw new ConfigureDSException(e,ERR_CONFIGDS_CANNOT_UPDATE_DIGEST_MD5_FQDN.get(e));
  }
}
```
Original comment:
```
Set the FQDN for the DIGEST-MD5 SASL mechanism.
```
Generated comment:
```
Adds a new host to the database.
```
---
id242
Code snippet:
```
public java.lang.String toString(){
  String xml=this.toString(true,false);
  return xml;
}
```
Original comment:
```
Returns a String representation of the element.
```
Generated comment:
```
Returns a string representation of this object.
```
---
id243
Code snippet:
```
public static String truncate(String str,int len){
  if (str == null) {
    return null;
  }
  if (len < 0) {
    return null;
  }
  if (str.length() > len) {
    return str.substring(0,len);
  }
 else {
    return str;
  }
}
```
Original comment:
```
truncate a string if it longer than the argument
```
Generated comment:
```
Truncate a string.
```
---
id244
Code snippet:
```
public SoftBevelBorder(int bevelType,Color highlight,Color shadow){
  super(bevelType,highlight,shadow);
}
```
Original comment:
```
Creates a bevel border with the specified type, highlight and shadow colors.
```
Generated comment:
```
Creates a bevel border with the specified colors.
```
---
id245
Code snippet:
```
@Override public void init(Subject subject,Map sharedState,Map options){
  this.sharedState=sharedState;
  authLoginModule.init(subject,sharedState,options);
}
```
Original comment:
```
Initialize this AuthLoginModule. <p> This is an abstract method, must be implemented by user\'s Login Module to initialize this AuthLoginModule with the relevant information. If this AuthLoginModule does not understand any of the data stored in sharedState or options parameters, they can be ignored.
```
Generated comment:
```
Initialize global variables.
```
---
id246
Code snippet:
```
public java.lang.Object newInstance(java.lang.Class javaContentInterface) throws javax.xml.bind.JAXBException {
  return super.newInstance(javaContentInterface);
}
```
Original comment:
```
Create an instance of the specified Java content interface.
```
Generated comment:
```
Creates a new instance.
```
---
id247
Code snippet:
```
@Override public int compare(AbstractIndexDescriptor index1,AbstractIndexDescriptor index2){
  int result;
  IndexDescriptor i1=(IndexDescriptor)index1;
  IndexDescriptor i2=(IndexDescriptor)index2;
  int[] possibleResults={compareNames(i1,i2),compareEntryLimits(i1,i2),compareTypes(i1,i2),compareRebuildRequired(i1,i2)};
  result=possibleResults[sortColumn];
  if (result == 0) {
    for (    int i : possibleResults) {
      if (i != 0) {
        result=i;
        break;
      }
    }
  }
  if (!sortAscending) {
    result=-result;
  }
  return result;
}
```
Original comment:
```
Comparable implementation.
```
Generated comment:
```
Searches for the index of the first occurence of the given argument, beginning the search at index, and testing for equality using the equals method.
```
---
id248
Code snippet:
```
public void actionPerformed(ActionEvent e){
  JTextComponent target=getTextComponent(e);
  if (target != null) {
    try {
      int offs=target.getCaretPosition();
      int endOffs=Utilities.getRowEnd(target,offs);
      if (select) {
        target.moveCaretPosition(endOffs);
      }
 else {
        target.setCaretPosition(endOffs);
      }
    }
 catch (    BadLocationException bl) {
      UIManager.getLookAndFeel().provideErrorFeedback(target);
    }
  }
}
```
Original comment:
```
The operation to perform when this action is triggered.
```
Generated comment:
```
The operation to perform when this action is triggered.
```
---
id249
Code snippet:
```
@Override public void flush(){
}
```
Original comment:
```
Calling this method has no effect.
```
Generated comment:
```
Flushes the output stream.
```
---
id250
Code snippet:
```
public static VirtualListViewResponseControl newControl(final int targetPosition,final int contentCount,final ResultCode result,final ByteString contextID){
  Reject.ifNull(result);
  Reject.ifFalse(targetPosition >= 0,\"targetPosition is less than 0\");
  Reject.ifFalse(contentCount >= 0,\"contentCount is less than 0\");
  return new VirtualListViewResponseControl(false,targetPosition,contentCount,result,contextID);
}
```
Original comment:
```
Creates a new virtual list view response control.
```
Generated comment:
```
Creates a new navigator.
```
---
id251
Code snippet:
```
public void destroy() throws org.omg.CosNaming.NamingContextPackage.NotEmpty {
  org.omg.CORBA.portable.InputStream $in=null;
  try {
    org.omg.CORBA.portable.OutputStream $out=_request(\"destroy\",true);
    $in=_invoke($out);
    return;
  }
 catch (  org.omg.CORBA.portable.ApplicationException $ex) {
    $in=$ex.getInputStream();
    String _id=$ex.getId();
    if (_id.equals(\"IDL:omg.org/CosNaming/NamingContext/NotEmpty:1.0\"))     throw org.omg.CosNaming.NamingContextPackage.NotEmptyHelper.read($in);
 else     throw new org.omg.CORBA.MARSHAL(_id);
  }
catch (  org.omg.CORBA.portable.RemarshalException $rm) {
    destroy();
  }
 finally {
    _releaseReply($in);
  }
}
```
Original comment:
```
The destroy operation deletes a naming context. If the naming  context contains bindings, the NotEmpty exception is raised.
```
Generated comment:
```
Destroys the stream.
```
---
id252
Code snippet:
```
public void deleteChar(AttributedCharacterIterator newParagraph,int deletePos){
  fStart=newParagraph.getBeginIndex();
  int end=newParagraph.getEndIndex();
  if (end - fStart != fChars.length - 1) {
    initAll(newParagraph);
  }
  char[] newChars=new char[end - fStart];
  int changedIndex=deletePos - fStart;
  System.arraycopy(fChars,0,newChars,0,deletePos - fStart);
  System.arraycopy(fChars,changedIndex + 1,newChars,changedIndex,end - deletePos);
  fChars=newChars;
  if (fBidi != null) {
    fBidi=new Bidi(newParagraph);
    if (fBidi.isLeftToRight()) {
      fBidi=null;
    }
  }
  fParagraph=StyledParagraph.deleteChar(newParagraph,fChars,deletePos,fParagraph);
  invalidateComponents();
}
```
Original comment:
```
Updates the <code>TextMeasurer</code> after a single character has been deleted from the paragraph currently represented by this <code>TextMeasurer</code>.  After this call, this <code>TextMeasurer</code> is equivalent to a new <code>TextMeasurer</code> created from the text;  however, it will usually be more efficient to update an existing <code>TextMeasurer</code> than to create a new one from scratch.
```
Generated comment:
```
Elimina un campo multivalor de tipo texto.
```
---
id253
Code snippet:
```
public static JTextArea createTextArea(LocalizableMessage text,int rows,int cols){
  JTextArea ta=new JTextArea(text.toString(),rows,cols);
  ta.setFont(ColorAndFontConstants.defaultFont);
  return ta;
}
```
Original comment:
```
Creates a text area.
```
Generated comment:
```
Creates a new <code>textarea</code>.
```
---
id254
Code snippet:
```
@Override public Foo fetchByUuid_First(String uuid,OrderByComparator<Foo> orderByComparator){
  List<Foo> list=findByUuid(uuid,0,1,orderByComparator);
  if (!list.isEmpty()) {
    return list.get(0);
  }
  return null;
}
```
Original comment:
```
Returns the first foo in the ordered set where uuid = &#63;.
```
Generated comment:
```
Fetch a list of entities.
```
---
id255
Code snippet:
```
static void writeEpochSec(long epochSec,DataOutput out) throws IOException {
  if (epochSec >= -4575744000L && epochSec < 10413792000L && epochSec % 900 == 0) {
    int store=(int)((epochSec + 4575744000L) / 900);
    out.writeByte((store >>> 16) & 255);
    out.writeByte((store >>> 8) & 255);
    out.writeByte(store & 255);
  }
 else {
    out.writeByte(255);
    out.writeLong(epochSec);
  }
}
```
Original comment:
```
Writes the state to the stream.
```
Generated comment:
```
Writes a long.
```
---
id256
Code snippet:
```
public void printStackTrace(PrintWriter s){
  super.printStackTrace(s);
  if (cause != null) {
    cause.printStackTrace(s);
  }
}
```
Original comment:
```
Prints this <code>XMLSignatureException</code>, its backtrace and the cause\'s backtrace to the specified print writer.
```
Generated comment:
```
Prints the stack trace to the specified print writer.
```
---
id257
Code snippet:
```
public PropertyDefinitionUsageBuilder(boolean isDetailed){
  this.pimpl=new MyPropertyDefinitionVisitor(isDetailed);
}
```
Original comment:
```
Creates a new property usage builder.
```
Generated comment:
```
Creates a new instance.
```
---
id258
Code snippet:
```
public void testPosNegFirstLonger(){
  String numA=\"2837462783428374767845648748973847593874837948575684767\";
  String numB=\"-293478573489347658763745839457637\";
  String res=\"-2837462783428374767845615168483972194300564226167553532\";
  BigInteger aNumber=new BigInteger(numA);
  BigInteger bNumber=new BigInteger(numB);
  BigInteger result=aNumber.xor(bNumber);
  assertTrue(res.equals(result.toString()));
}
```
Original comment:
```
Xor for a positive and a negative numbers; the first is longer
```
Generated comment:
```
Xor for two positive numbers.
```
---
id259
Code snippet:
```
protected boolean isValidQName(String prefix,String local,boolean xml11Version){
  if (local == null)   return false;
  boolean validNCName=false;
  if (!xml11Version) {
    validNCName=(prefix == null || XMLChar.isValidNCName(prefix)) && XMLChar.isValidNCName(local);
  }
 else {
    validNCName=(prefix == null || XML11Char.isXML11ValidNCName(prefix)) && XML11Char.isXML11ValidNCName(local);
  }
  return validNCName;
}
```
Original comment:
```
Taken from org.apache.xerces.dom.CoreDocumentImpl Checks if the given qualified name is legal with respect to the version of XML to which this document must conform.
```
Generated comment:
```
Returns true if the name is valid.
```
---
id260
Code snippet:
```
public boolean baseIsLeftToRight(){
  return bidiBase.baseIsLeftToRight();
}
```
Original comment:
```
Return true if the base direction is left-to-right.
```
Generated comment:
```
Returns true if this is a right-to-left.
```
---
id261
Code snippet:
```
public static String generateMessageHandleWithServerID(){
  if (random == null) {
    return null;
  }
  byte bytes[]=new byte[SAML2Constants.ID_LENGTH];
  random.nextBytes(bytes);
  String id=byteArrayToString(bytes);
  return embedServerID(id);
}
```
Original comment:
```
Generates message handle with server id used in an <code>Artifact</code>.
```
Generated comment:
```
Generate a salt for use with the bcrypt.hashpw() method.
```
---
id262
Code snippet:
```
protected void paintPath(int operation,int rule){
  PathRenderInfo renderInfo=new PathRenderInfo(currentPath,operation,rule,isClip,clippingRule,getGraphicsState());
  eventOccurred(renderInfo,EventType.RENDER_PATH);
  if (isClip) {
    isClip=false;
    ParserGraphicsState gs=getGraphicsState();
    gs.clip(currentPath,clippingRule);
    eventOccurred(new ClippingPathInfo(gs.getClippingPath(),gs.getCtm()),EventType.CLIP_PATH_CHANGED);
  }
  currentPath=new Path();
}
```
Original comment:
```
Displays the current path.
```
Generated comment:
```
Document me!.
```
---
id263
Code snippet:
```
public boolean hasWrongStatus(){
  return hasWrongStatus;
}
```
Original comment:
```
Gets the wrong status marker for the future update ack.
```
Generated comment:
```
Returns whether it has the status.
```
---
id264
Code snippet:
```
public void testCase24(){
  byte rBytes[]={0};
  BigInteger aNumber=BigInteger.ONE;
  BigInteger bNumber=BigInteger.ONE;
  BigInteger result=aNumber.subtract(bNumber);
  byte resBytes[]=new byte[rBytes.length];
  resBytes=result.toByteArray();
  for (int i=0; i < resBytes.length; i++) {
    assertTrue(resBytes[i] == rBytes[i]);
  }
  assertEquals(0,result.signum());
}
```
Original comment:
```
Subtract ONE from ONE.
```
Generated comment:
```
Subtract two numbers of the same length and different signs. the first is positive.
```
---
id265
Code snippet:
```
private Object createSipFactory(String objectClassName) throws PeerUnavailableException {
  if (objectClassName == null) {
    throw new NullPointerException();
  }
  try {
    Class peerObjectClass=Class.forName(getPathName() + \".\" + objectClassName);
    Object newPeerObject=peerObjectClass.newInstance();
    return (newPeerObject);
  }
 catch (  Exception e) {
    String errmsg=\"The Peer Factory: \" + getPathName() + \".\"+ objectClassName+ \" could not be instantiated. Ensure the Path Name has been set.\";
    throw new PeerUnavailableException(errmsg,e);
  }
}
```
Original comment:
```
Private Utility method used by all create methods to return an instance of the supplied object.
```
Generated comment:
```
Creates a new instance.
```
---
id266
Code snippet:
```
public SRGLoader(Map<String,ClassNode> nodes){
  super(nodes);
  useNodes=true;
}
```
Original comment:
```
Instantiates the loader with a map of classnodes to be mapped.
```
Generated comment:
```
Creates a new instance.
```
---
id267
Code snippet:
```
MultistepExprHolder unlink(MultistepExprHolder itemToRemove){
  MultistepExprHolder first=this;
  MultistepExprHolder next=this;
  MultistepExprHolder prev=null;
  while (null != next) {
    if (next == itemToRemove) {
      if (null == prev)       first=next.m_next;
 else       prev.m_next=next.m_next;
      next.m_next=null;
      return first;
    }
    prev=next;
    next=next.m_next;
  }
  assertion(false,\"unlink failed!!!\");
  return null;
}
```
Original comment:
```
Remove the given element from the list.  \'this\' should  be the head of the list.  If the item to be removed is not  found, an assertion will be made.
```
Generated comment:
```
Returns the next element in the list.
```
---
id268
Code snippet:
```
public BasicAttributes(boolean ignoreCase){
  this.ignoreCase=ignoreCase;
}
```
Original comment:
```
Constructs a new instance of Attributes. If <code>ignoreCase</code> is true, the character case of attribute identifiers is ignored; otherwise the case is significant.
```
Generated comment:
```
Creates a new attribute.
```
---
id269
Code snippet:
```
private int[] parseMonths(String line){
  int[] months=new int[12];
  String[] numbers=line.split(\"\\s\");
  if (numbers.length != 12) {
    throw new IllegalArgumentException(\"wrong number of months on line: \" + Arrays.toString(numbers) + \"; count: \"+ numbers.length);
  }
  for (int i=0; i < 12; i++) {
    try {
      months[i]=Integer.valueOf(numbers[i]);
    }
 catch (    NumberFormatException nfe) {
      throw new IllegalArgumentException(\"bad key: \" + numbers[i]);
    }
  }
  return months;
}
```
Original comment:
```
Parses the 12 months lengths from a property value for a specific year.
```
Generated comment:
```
Parse a string value to a calendar.
```
---
id270
Code snippet:
```
@After public void unregisterIdlingResource(){
  Espresso.unregisterIdlingResources(mAddTaskIntentsTestRule.getActivity().getCountingIdlingResource());
}
```
Original comment:
```
Unregister your Idling Resource so it can be garbage collected and does not leak any memory.
```
Generated comment:
```
Unregister all resources.
```
---
id271
Code snippet:
```
final Node succ(Node p){
  Node next=p.next;
  return (p == next) ? head : next;
}
```
Original comment:
```
Returns the successor of p, or the head node if p.next has been linked to self, which will only be true if traversing with a stale pointer that is now off the list.
```
Generated comment:
```
Get the next node in the iteration.
```
---
id272
Code snippet:
```
public void recycle(){
  decoder.reset();
  leftovers.position(0);
}
```
Original comment:
```
Reset the decoder state.
```
Generated comment:
```
Reset the iterator to the last marked position.
```
---
id273
Code snippet:
```
static void putRealm(JsonValue jsonValue,String value){
  jsonValue.put(EVENT_REALM,value);
}
```
Original comment:
```
Set \"realm\" audit log field.
```
Generated comment:
```
Inserts a long value into the mapping of this bundle, replacing any existing value for the given key. either key or value may be null.
```
---
id274
Code snippet:
```
@SuppressWarnings(\"rawtypes\") public LocalCache(String name,int maxSize,long maxLifetime){
  this.name=name;
  this.maxCacheSize=maxSize;
  this.defaultLifetime=maxLifetime;
  map=new HashMap(103);
  lastAccessedList=new LinkedList();
  ageList=new LinkedList();
}
```
Original comment:
```
Create a new cache and specify the maximum size of for the cache in bytes, and the maximum lifetime of objects.
```
Generated comment:
```
Creates a new cache.
```
---
id275
Code snippet:
```
public HyphenationException(String msg){
  super(msg);
}
```
Original comment:
```
Construct a hyphenation exception.
```
Generated comment:
```
Constructs a new exception with the specified detail message. the cause is not initialized.
```
---
id276
Code snippet:
```
@Override public void send(HandshakeIODataStream out){
}
```
Original comment:
```
Sends message
```
Generated comment:
```
Sends a message to the server.
```
---
id277
Code snippet:
```
public void installUI(JComponent c){
  super.installUI(c);
  MetalToolBarUI.register(c);
}
```
Original comment:
```
Configures the specified component appropriate for the metal look and feel.
```
Generated comment:
```
Invokes the <code>installui</code> method on each ui handled by this object.
```
---
id278
Code snippet:
```
public boolean startsWith(XMLString prefix){
  return startsWith(prefix,0);
}
```
Original comment:
```
Tests if this string starts with the specified prefix.
```
Generated comment:
```
Returns true if the specified namespace uri matches the specified prefix.
```
---
id279
Code snippet:
```
@Override public final void run(){
  setProcessingStartTime();
  getPluginConfigManager().invokePreParseUnbindPlugins(this);
  logUnbind(this);
  getClientConnection().disconnect(DisconnectReason.UNBIND,false,null);
  getPluginConfigManager().invokePostOperationUnbindPlugins(this);
  setProcessingStopTime();
}
```
Original comment:
```
Performs the work of actually processing this operation.  This should include all processing for the operation, including invoking plugins, logging messages, performing access control, managing synchronization, and any other work that might need to be done in the course of processing.
```
Generated comment:
```
Start the server.
```
---
id280
Code snippet:
```
public static Bitmap resizeImageByWidth(Bitmap image){
  if (image == null) {
    throw new NullPointerException(\"Bitmap not set!\");
  }
  int newHeight=(image.getHeight() * getMaxSizeInPixel()) / image.getWidth();
  return Bitmap.createScaledBitmap(image,getMaxSizeInPixel(),newHeight,true);
}
```
Original comment:
```
Resizes the image by only its width.
```
Generated comment:
```
Resize the image to the specified width and height.
```
---
id281
Code snippet:
```
public static int csnsUTF8(int nbFields){
  return CSN.STRING_ENCODING_LENGTH * nbFields + 1;
}
```
Original comment:
```
Helper method that returns the number of bytes that would be used by the CSN fields encoded as a UTF8 string when appended to a ByteArrayBuilder.
```
Generated comment:
```
Returns the result of interpreting the object as an instance of \'<em>int</em>\'. <!-- begin-user-doc --> this implementation returns null; returning a non-null result will terminate the switch. <!-- end-user-doc -->.
```
---
id282
Code snippet:
```
public StoreFileMover(String basename,String filename,String encoding){
  setBasename(basename);
  setEncoding(encoding);
  setFilename(filename);
  init();
}
```
Original comment:
```
Calculate file objects for the old and new configuration files.
```
Generated comment:
```
Creates a new instance.
```
---
id283
Code snippet:
```
public OutputStream bindStream(OutputStream output){
  OutputStream stream=m_streams.get();
  m_streams.set(output);
  return stream;
}
```
Original comment:
```
Bind the specified stream to the current thread.
```
Generated comment:
```
Binds the given output stream to the output stream.
```
---
id284
Code snippet:
```
public void paintSeparatorForeground(SynthContext context,Graphics g,int x,int y,int w,int h,int orientation){
}
```
Original comment:
```
Paints the foreground of a separator.
```
Generated comment:
```
Paints the specified component.
```
---
id285
Code snippet:
```
public boolean isFullSpan(){
  return this.fullSpan;
}
```
Original comment:
```
Checks whether or not the region have a full span. <P>
```
Generated comment:
```
Returns true if the span is empty.
```
---
id286
Code snippet:
```
public InvalidKeyException(){
  super();
}
```
Original comment:
```
An InvalidKeyException with no detail message.
```
Generated comment:
```
Constructs a new exception with <code>null</code> as its detail message. the cause is not initialized.
```
---
id287
Code snippet:
```
ConstantClass(final DataInput file) throws IOException {
  super(Const.CONSTANT_Class);
  this.name_index=file.readUnsignedShort();
}
```
Original comment:
```
Initialize instance from file data.
```
Generated comment:
```
Creates a new instance of <code>datainput</code>.
```
---
id288
Code snippet:
```
public FrameBodyTSIZ(ByteBuffer byteBuffer,int frameSize) throws InvalidTagException {
  super(byteBuffer,frameSize);
}
```
Original comment:
```
Creates a new FrameBodyTSIZ datatype.
```
Generated comment:
```
Constructs a <code>bufferedimage</code>.
```
---
id289
Code snippet:
```
private void enableMapper() throws Exception {
  replace(\"cn=EXTERNAL,cn=SASL Mechanisms,cn=config\",\"ds-cfg-certificate-mapper\",FINGERPRINT_MAPPER_DN);
}
```
Original comment:
```
Alters the configuration of the SASL EXTERNAL mechanism handler so that it uses the Subject DN to User Attribute certificate mapper.
```
Generated comment:
```
Enables the mbean server.
```
---
id290
Code snippet:
```
public void paintToolBarDragWindowBackground(SynthContext context,Graphics g,int x,int y,int w,int h){
  paintBackground(context,g,x,y,w,h,null);
}
```
Original comment:
```
Paints the background of the window containing the tool bar when it has been detached from its primary frame.
```
Generated comment:
```
Paints the background of a slider. this implementation invokes the method of the same name without the orientation.
```
---
id291
Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(hc_elementgetattributenodenull.class,args);
}
```
Original comment:
```
Runs this test from the command line.
```
Generated comment:
```
Runs this test from the command line.
```
---
id292
Code snippet:
```
@Override public boolean isReady(){
  return false;
}
```
Original comment:
```
TODO SERVLET 3.1
```
Generated comment:
```
Returns <code>true</code>.
```
---
id293
Code snippet:
```
public InvalidCredentialsException(){
  super();
}
```
Original comment:
```
Creates a new InvalidCredentialsException with a <tt>null</tt> detail message.
```
Generated comment:
```
Constructs a new exception with <code>null</code> as its detail message. the cause is not initialized.
```
---
id294
Code snippet:
```
public String toString(){
  StringBuffer sb=new StringBuffer(200);
  sb.append(\"<RemoveEntry xmlns=\\"\").append(DiscoConstants.DISCO_NS).append(\"\\"\");
  if (entryID != null) {
    sb.append(\" entryID=\\"\").append(entryID).append(\"\\"\");
  }
  sb.append(\"></RemoveEntry>\");
  return sb.toString();
}
```
Original comment:
```
Returns string format.
```
Generated comment:
```
String representation.
```
---
id295
Code snippet:
```
Script reparse(String className,String text) throws CompilationFailedException {
  return super.parse(new GroovyCodeSource(text,className,DEFAULT_CODE_BASE));
}
```
Original comment:
```
Used internally to reload the script back when coming back from the persisted state (therefore we don\'t want to record this.)
```
Generated comment:
```
Create a script from a string.
```
---
id296
Code snippet:
```
@SuppressWarnings(\"unchecked\") public Enumeration<Permission> elements(){
synchronized (this) {
    return Collections.enumeration((List<Permission>)(List)perms);
  }
}
```
Original comment:
```
Returns an enumeration of all the SocketPermission objects in the container.
```
Generated comment:
```
Returns an enumeration of all the permissions.
```
---
id297
Code snippet:
```
@DataProvider(name=\"createSubordinateTestData\") public Object[][] createSubordinateTestData(){
  return new Object[][]{{\"\",\"\",true},{\"\",\"dc=org\",false},{\"\",\"dc=opendj,dc=org\",false},{\"\",\"dc=foo,dc=opendj,dc=org\",false},{\"dc=org\",\"\",true},{\"dc=org\",\"dc=org\",true},{\"dc=org\",\"dc=opendj,dc=org\",false},{\"dc=org\",\"dc=foo,dc=opendj,dc=org\",false},{\"dc=opendj,dc=org\",\"\",true},{\"dc=opendj,dc=org\",\"dc=org\",true},{\"dc=opendj,dc=org\",\"dc=opendj,dc=org\",true},{\"dc=opendj,dc=org\",\"dc=foo,dc=opendj,dc=org\",false},{\"dc=foo,dc=opendj,dc=org\",\"\",true},{\"dc=foo,dc=opendj,dc=org\",\"dc=org\",true},{\"dc=foo,dc=opendj,dc=org\",\"dc=opendj,dc=org\",true},{\"dc=foo,dc=opendj,dc=org\",\"dc=foo,dc=opendj,dc=org\",true},{\"dc=org\",\"dc=com\",false},{\"dc=opendj,dc=org\",\"dc=foo,dc=org\",false},{\"dc=opendj,dc=org\",\"dc=opendj,dc=com\",false}};
}
```
Original comment:
```
Subordinate test data provider.
```
Generated comment:
```
Creates a new data source.
```
---
id298
Code snippet:
```
public void remove(BrdItem p_item){
  if (!p_item.is_on_the_board())   return;
  for (  AwtreeShapeSearch curr_tree : search_trees) {
    AwtreeNodeLeaf[] curr_tree_entries=p_item.get_search_tree_entries(curr_tree);
    if (curr_tree_entries == null)     continue;
    curr_tree.remove(curr_tree_entries);
  }
  p_item.clear_search_tree_entries();
  p_item.set_on_the_board(false);
}
```
Original comment:
```
Removes all entries of an item from the search trees.
```
Generated comment:
```
Removes an item from the tree.
```
---
id299
Code snippet:
```
public boolean canContinueReading(){
  return canContinueReading;
}
```
Original comment:
```
Indicates whether the nature of this exception allows the caller to continue reading LDIF data.  If this method returns <CODE>false</CODE>, then the associated reader should be closed by the caller.
```
Generated comment:
```
Gets the value of the isscorable property.
```
---
id300
Code snippet:
```
public MapFailedException(java.io.IOException e){
  super(e.getMessage());
  initCause(e);
}
```
Original comment:
```
Creates a new MapFailedException.
```
Generated comment:
```
Constructs a new <code>cacheclientinfoexception</code> with the specified detail message. the cause is not initialized.
```
---
id301
Code snippet:
```
public RESTEndpointBuilder apiVersion(String apiVersion){
  headers.put(\"Accept-API-Version\",\"protocol=1.0,resource=\" + apiVersion);
  return this;
}
```
Original comment:
```
Set the API version for this endpoint.
```
Generated comment:
```
*optional sets the id to the provided value.
```
---
id302
Code snippet:
```
public AttributeMissingException(Throwable cause){
  super(cause);
}
```
Original comment:
```
Constructs a new exception with the specified cause.
```
Generated comment:
```
Constructs a new exception with the specified detail message, cause, and bean for jax-ws exception serialization.
```
---
id303
Code snippet:
```
private boolean complete_expansion_room(ExpandRoomFreespaceIncomplete p_incomplete_room){
  Collection<ExpandRoomFreespaceComplete> completed_rooms=autoroute_engine.complete_expansion_room(p_incomplete_room);
  return (completed_rooms.size() > 0);
}
```
Original comment:
```
Returns true, if the completion succeeded.
```
Generated comment:
```
Returns true if the specified collection contains the specified element.
```
---
id304
Code snippet:
```
@Restricted(NoExternalUse.class) public String iotaStr(){
  return String.valueOf(iota());
}
```
Original comment:
```
Assigns a new ID.
```
Generated comment:
```
Returns a string representation of this object.
```
---
id305
Code snippet:
```
public CompletedLoginProcess(LoginAuthenticator loginAuthenticator,LoginConfiguration loginConfiguration,CoreServicesWrapper coreServicesWrapper,SSOToken ssoToken){
  super(loginAuthenticator,loginConfiguration,null,coreServicesWrapper);
  this.ssoToken=ssoToken;
  orgDn=coreServicesWrapper.getDomainNameByRequest(loginConfiguration.getHttpRequest());
}
```
Original comment:
```
Constructs an instance of the LoginProcess.
```
Generated comment:
```
Creates a new instance.
```
---
id306
Code snippet:
```
public Future<Long> cardByType(String type,JobState state){
  Future<Long> future=Future.future();
  jobService.cardByType(type,state,future.completer());
  return future;
}
```
Original comment:
```
Get cardinality by job type and state.
```
Generated comment:
```
Asynchronous setup.
```
---
id307
Code snippet:
```
public static String postRequest(URL url,String postData,String encoding,String contentType,int readTimeout,int socketTimeout){
  return postRequest(url,postData,encoding,contentType,false,readTimeout,socketTimeout);
}
```
Original comment:
```
Sends a POST request
```
Generated comment:
```
Creates a new request.
```
---
id308
Code snippet:
```
public static boolean callsSuper(MethodNode mn){
  for (  AbstractInsnNode ain : mn.instructions.toArray()) {
    if (ain.getOpcode() == Opcodes.INVOKESPECIAL) {
      MethodInsnNode min=(MethodInsnNode)ain;
      if (min.name.equals(mn.name)) {
        return true;
      }
    }
  }
  return false;
}
```
Original comment:
```
Returns true if the method has called it\'s super method.
```
Generated comment:
```
Returns true if the given instruction is a call to this method.
```
---
id309
Code snippet:
```
@TargetApi(Build.VERSION_CODES.JELLY_BEAN_MR2) private AutoInstallsLayout createWorkspaceLoaderFromAppRestriction(){
  if (!Utilities.ATLEAST_JB_MR2) {
    return null;
  }
  Context ctx=getContext();
  UserManager um=(UserManager)ctx.getSystemService(Context.USER_SERVICE);
  Bundle bundle=um.getApplicationRestrictions(ctx.getPackageName());
  if (bundle == null) {
    return null;
  }
  String packageName=bundle.getString(RESTRICTION_PACKAGE_NAME);
  if (packageName != null) {
    try {
      Resources targetResources=ctx.getPackageManager().getResourcesForApplication(packageName);
      return AutoInstallsLayout.get(ctx,packageName,targetResources,mOpenHelper.mAppWidgetHost,mOpenHelper);
    }
 catch (    NameNotFoundException e) {
      Log.e(TAG,\"Target package for restricted profile not found\",e);
      return null;
    }
  }
  return null;
}
```
Original comment:
```
Creates workspace loader from an XML resource listed in the app restrictions.
```
Generated comment:
```
Creates a new instance of this fragment.
```
---
id310
Code snippet:
```
public void constrainDrawRect(int left,int top,int right,int bottom){
  contentRect.set(left,top,right,bottom);
}
```
Original comment:
```
Set left/top/right/bottom values of drawing rect (area where graph will draw)
```
Generated comment:
```
Set the overall size for the progress spinner. this updates the radius and stroke width of the ring.
```
---
id311
Code snippet:
```
public DefaultFormatter(){
  overwriteMode=true;
  allowsInvalid=true;
}
```
Original comment:
```
Creates a DefaultFormatter.
```
Generated comment:
```
Creates a new instance.
```
---
id312
Code snippet:
```
void selectField(Object f,int count){
  AttributedCharacterIterator iterator=getIterator();
  if (iterator != null && (f instanceof AttributedCharacterIterator.Attribute)) {
    AttributedCharacterIterator.Attribute field=(AttributedCharacterIterator.Attribute)f;
    iterator.first();
    while (iterator.current() != CharacterIterator.DONE) {
      while (iterator.getAttribute(field) == null && iterator.next() != CharacterIterator.DONE)       ;
      if (iterator.current() != CharacterIterator.DONE) {
        int limit=iterator.getRunLimit(field);
        if (--count <= 0) {
          getFormattedTextField().select(iterator.getIndex(),limit);
          break;
        }
        iterator.setIndex(limit);
        iterator.next();
      }
    }
  }
}
```
Original comment:
```
Selects the fields identified by <code>attributes</code>.
```
Generated comment:
```
Selects the attribute at the given index.
```
---
id313
Code snippet:
```
public byte[] toByteArray(){
  byte[] newbuf=new byte[count];
  System.arraycopy(buf,0,newbuf,0,count);
  return newbuf;
}
```
Original comment:
```
Creates a newly allocated byte array. Its size is the current size of this output stream and the valid contents of the buffer have been copied into it.
```
Generated comment:
```
Gets the curent contents of this byte stream as a byte array. the result is independent of this stream.
```
---
id314
Code snippet:
```
public void doGroupAction(Object obj){
  if (target != null) {
    target.doGroupAction(obj);
  }
}
```
Original comment:
```
The function to be run on the objects when there is time.
```
Generated comment:
```
This method was generated by mybatis generator. this method corresponds to the database table group.
```
---
id315
Code snippet:
```
public com.sun.identity.wsfederation.jaxb.wsu.CreatedElement createCreatedElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.wsfederation.jaxb.wsu.impl.CreatedElementImpl();
}
```
Original comment:
```
Create an instance of CreatedElement
```
Generated comment:
```
Creates a new instance.
```
---
id316
Code snippet:
```
public synchronized void addDropTargetListener(DropTargetListener dtl) throws TooManyListenersException {
  if (dtl == null)   return;
  if (equals(dtl))   throw new IllegalArgumentException(\"DropTarget may not be its own Listener\");
  if (dtListener == null)   dtListener=dtl;
 else   throw new TooManyListenersException();
}
```
Original comment:
```
Adds a new <code>DropTargetListener</code> (UNICAST SOURCE). <P>
```
Generated comment:
```
Add listener.
```
---
id317
Code snippet:
```
public boolean isRepresentationClassReader(){
  return java.io.Reader.class.isAssignableFrom(representationClass);
}
```
Original comment:
```
Returns whether the representation class for this <code>DataFlavor</code> is <code>java.io.Reader</code> or a subclass thereof.
```
Generated comment:
```
Returns <code>true</code> if the class is a subclass of <code>java.lang.class</code>.
```
---
id318
Code snippet:
```
private FakeReplicationDomain createFakeReplicationDomain(int serverId,int groupId,int rsId,long generationId,AssuredMode assuredMode,int safeDataLevel,long assuredTimeout,int scenario,ServerState serverState,boolean startListen) throws Exception {
  final DomainFakeCfg config=newDomainConfig(serverId,groupId,rsId,assuredMode,safeDataLevel,assuredTimeout);
  return createFakeReplicationDomain(config,rsId,generationId,scenario,serverState,startListen);
}
```
Original comment:
```
Creates a new fake replication domain, using the passed scenario.
```
Generated comment:
```
Create a new cluster.
```
---
id319
Code snippet:
```
public void init(ServletConfig config) throws ServletException {
  super.init(config);
  if (!AMSetupServlet.isCurrentConfigurationValid()) {
    return;
  }
  if (WebtopNaming.configMonitoring() == 0) {
    ConfigMonitoring cm=new ConfigMonitoring();
    cm.configureMonitoring();
  }
}
```
Original comment:
```
Initializes the servlet.  This method does all the \"work\" of gathering the configuration information for, and passing it to the Monitoring service.
```
Generated comment:
```
Initialize global variables.
```
---
id320
Code snippet:
```
public int read(long position,byte[] buffer,int offset,int length) throws IOException {
  checkStream();
  final int n=input.read(position,buffer,offset,length);
  if (n > 0) {
    decrypt(position,buffer,offset,n);
  }
  return n;
}
```
Original comment:
```
Reads up to the specified number of bytes from a given position within a stream and return the number of bytes read. This does not change the current offset of the stream, and is thread-safe.
```
Generated comment:
```
Reads a sequence of bytes from this file into the given buffer, starting at the given offset.
```
---
id321
Code snippet:
```
public void insert_any(org.omg.CORBA.Any value) throws org.omg.DynamicAny.DynAnyPackage.TypeMismatch, org.omg.DynamicAny.DynAnyPackage.InvalidValue {
  org.omg.CORBA.portable.ServantObject $so=_servant_preinvoke(\"insert_any\",_opsClass);
  DynAnyOperations $self=(DynAnyOperations)$so.servant;
  try {
    $self.insert_any(value);
  }
  finally {
    _servant_postinvoke($so);
  }
}
```
Original comment:
```
Inserts an Any value into the Any represented by this DynAny.
```
Generated comment:
```
Inserts the specified object at the specified position in this list. shifts the element currently at that position (if any) and any subsequent elements to the right (adds one to their indices).
```
---
id322
Code snippet:
```
public boolean beginErrorBlockDisplay(ChildDisplayEvent event){
  if (model.isError()) {
    setDisplayFieldValue(ERROR_TITLE,model.getErrorTitle());
    setDisplayFieldValue(ERROR_MSG,model.getErrorMessage());
    return true;
  }
  return false;
}
```
Original comment:
```
Begins error message content
```
Generated comment:
```
Returns true if the specified event is a block.
```
---
id323
Code snippet:
```
public final Set<AwtreeObject> overlapping_objects(ShapeConvex p_shape,int p_layer){
  return search_tree_manager.get_default_tree().find_overlap_objects(p_shape,p_layer,NetNosList.EMPTY);
}
```
Original comment:
```
Returns all SearchTreeObjects on layer p_layer, which overlap with p_shape. If p_layer < 0, the layer is ignored
```
Generated comment:
```
Returns the index of the first point in the polygon.
```
---
id324
Code snippet:
```
public void endElement(String uri,String localName,String qName) throws SAXException {
  if (contentHandler != null) {
    contentHandler.endElement(uri,localName,qName);
  }
}
```
Original comment:
```
Filter an end element event.
```
Generated comment:
```
Receive notification of the end of an element.
```
---
id325
Code snippet:
```
public ProviderNotFoundException(final Class<? extends Provider> providerClass,final String providerName,final String message){
  super(message);
  this.providerType=providerClass;
  this.providerName=providerName;
}
```
Original comment:
```
Creates the exception with a provider type, provider name and a message.
```
Generated comment:
```
Constructs a new exception with the specified detail message. the cause is not initialized.
```
---
id326
Code snippet:
```
public void enableLogging(){
}
```
Original comment:
```
Enable logging (globally).
```
Generated comment:
```
Enables logging for this logger.
```
---
id327
Code snippet:
```
@AfterClass public static void cleanupClass(){
  try {
    Misc.deleteDirectorySimple(scenario.getRepositoryLocation());
  }
 catch (  Exception ignore) {
    System.err.println(\"cannot remove \" + scenario.getRepositoryLocation());
  }
}
```
Original comment:
```
Cleanup the whole junit scenario ; deletes the created git repository.
```
Generated comment:
```
Cleans up a class.
```
---
id328
Code snippet:
```
@Override protected void initializeInjector(ApplicationComponent applicationComponent){
  applicationComponent.inject(this);
  comicsComponent=DaggerComicsComponent.builder().applicationComponent(applicationComponent).activityModule(new ActivityModule(this)).comicsModule(new ComicsModule()).build();
}
```
Original comment:
```
Initialize injections by field.
```
Generated comment:
```
Initialize the component.
```
---
id329
Code snippet:
```
public InvalidConfigurationException(String msg){
  super(msg);
}
```
Original comment:
```
Constructs an instance of InvalidConfigurationException with the specified message.
```
Generated comment:
```
Constructs a new exception with the specified detail message. the cause is not initialized.
```
---
id330
Code snippet:
```
public static void initializePropertyDefinition(PropertyDefinition<?> propertyDef) throws Exception {
  propertyDef.initialize();
  propertyDef.getDefaultBehaviorProvider().initialize();
}
```
Original comment:
```
Initializes a property definition and its default behavior.
```
Generated comment:
```
Initialize the property.
```
---
id331
Code snippet:
```
public SplittableRandom(){
  long s=defaultGen.getAndAdd(2 * GOLDEN_GAMMA);
  this.seed=mix64(s);
  this.gamma=mixGamma(s + GOLDEN_GAMMA);
}
```
Original comment:
```
Creates a new SplittableRandom instance that is likely to generate sequences of values that are statistically independent of those of any other instances in the current program; and may, and typically does, vary across program invocations.
```
Generated comment:
```
Creates a new splittablerandom.
```
---
id332
Code snippet:
```
@Override public String toString(){
  return (\"ContainerEvent[\'\" + getContainer() + \"\',\'\"+ getType()+ \"\',\'\"+ getData()+ \"\']\");
}
```
Original comment:
```
Return a string representation of this event.
```
Generated comment:
```
Returns a string representation of this event.
```
---
id333
Code snippet:
```
protected Expression arg(int opPos) throws TransformerException {
  return compile(opPos + 2);
}
```
Original comment:
```
Compile a function argument.
```
Generated comment:
```
Compile a template.
```
---
id334
Code snippet:
```
public void createSubConfig(String name,String schemaName,Map values) throws AMConsoleException {
  String[] params={serviceName,parentConfig.getComponentName(),name,schemaName};
  try {
    amModel.logEvent(\"ATTEMPT_CREATE_GLOBAL_SUB_CONFIGURATION\",params);
    parentConfig.addSubConfig(name,schemaName,0,values);
    amModel.logEvent(\"SUCCEED_CREATE_GLOBAL_SUB_CONFIGURATION\",params);
  }
 catch (  SSOException e) {
    String[] paramsEx={serviceName,parentConfig.getComponentName(),name,schemaName,amModel.getErrorString(e)};
    amModel.logEvent(\"SSO_EXCEPTION_CREATE_GLOBAL_SUB_CONFIGURATION\",paramsEx);
    throw new AMConsoleException(amModel.getErrorString(e));
  }
catch (  SMSException e) {
    String[] paramsEx={serviceName,parentConfig.getComponentName(),name,schemaName,amModel.getErrorString(e)};
    amModel.logEvent(\"SMS_EXCEPTION_CREATE_GLOBAL_SUB_CONFIGURATION\",paramsEx);
    throw new AMConsoleException(amModel.getErrorString(e));
  }
}
```
Original comment:
```
Creates a new sub configuration.
```
Generated comment:
```
Creates a new configuration object.
```
---
id335
Code snippet:
```
private void writeObject(ObjectOutputStream s) throws java.io.IOException {
  s.defaultWriteObject();
  s.writeObject(toString());
}
```
Original comment:
```
Serializes only the unparsed DN, for compactness and to avoid any implementation dependency.
```
Generated comment:
```
Provides serialization support.
```
---
id336
Code snippet:
```
protected void sendCreateSession(String sessionId,DeltaSession session){
  if (cluster.getMembers().length > 0) {
    SessionMessage msg=new SessionMessageImpl(getName(),SessionMessage.EVT_SESSION_CREATED,null,sessionId,sessionId + \"-\" + System.currentTimeMillis());
    if (log.isDebugEnabled()) {
      log.debug(sm.getString(\"deltaManager.sendMessage.newSession\",name,sessionId));
    }
    msg.setTimestamp(session.getCreationTime());
    counterSend_EVT_SESSION_CREATED++;
    send(msg);
  }
}
```
Original comment:
```
Send create session event to all backup node
```
Generated comment:
```
Send a message to the session.
```
---
id337
Code snippet:
```
private void quitClicked(){
  application.quitClicked(getCurrentStep(),this);
}
```
Original comment:
```
Method called when user clicks \'Quit\' button of the wizard.
```
Generated comment:
```
This method is called when the user presses the back button.
```
---
id338
Code snippet:
```
private void highLightMarker(int index){
  highLightMarker(markers.get(index));
}
```
Original comment:
```
Highlight the marker by index.
```
Generated comment:
```
Highlights the specified line.
```
---
id339
Code snippet:
```
public static NSObject parse(InputStream in) throws ParseException, IOException {
  byte[] buf=PropertyListParser.readAll(in);
  in.close();
  return parse(buf);
}
```
Original comment:
```
Parses an ASCII property list from an input stream.
```
Generated comment:
```
Read a list of objects from an input stream.
```
---
id340
Code snippet:
```
private static String keyDump(Tree index,ByteSequence key){
  StringBuilder buffer=new StringBuilder(128);
  buffer.append(\"Index: \").append(index).append(ServerConstants.EOL);
  buffer.append(\"Key:\").append(ServerConstants.EOL);
  StaticUtils.byteArrayToHexPlusAscii(buffer,key.toByteArray(),6);
  return buffer.toString();
}
```
Original comment:
```
Construct a printable string from a raw key value.
```
Generated comment:
```
Returns a string representation of this object.
```
---
id341
Code snippet:
```
private static boolean copy(JsonValue subject,PatchOperation operation) throws BadRequestException {
  if (!operation.isCopy()) {
    throw new BadRequestException(\"Operation is a \" + operation.getOperation() + \", not a copy!\");
  }
  JsonValue value=subject.get(operation.getFrom());
  if (value == null || value.isNull()) {
    return false;
  }
  subject.add(operation.getField(),value.getObject());
  return true;
}
```
Original comment:
```
Apply a copy patch operation
```
Generated comment:
```
Creates a new operation.
```
---
id342
Code snippet:
```
public String encode(){
  return new StringBuilder().append(TIME_FIELD).append(startTime).append(Separators.SP).append(stopTime).append(Separators.NEWLINE).toString();
}
```
Original comment:
```
Get the string encoded version of this object
```
Generated comment:
```
Returns a string representation of this object.
```
---
id343
Code snippet:
```
public static void dropTable(SQLiteDatabase db,boolean ifExists){
  String sql=\"DROP TABLE \" + (ifExists ? \"IF EXISTS \" : \"\") + \"\\"CUSTOMER\\"\";
  db.execSQL(sql);
}
```
Original comment:
```
Drops the underlying database table.
```
Generated comment:
```
Drops the underlying database table.
```
---
id344
Code snippet:
```
protected void resetCipher(long position) throws IOException {
  final long counter=getCounter(position);
  CtrCryptoInputStream.calculateIV(initIV,counter,iv);
  try {
    cipher.init(Cipher.DECRYPT_MODE,key,new IvParameterSpec(iv));
  }
 catch (  InvalidKeyException e) {
    throw new IOException(e);
  }
catch (  InvalidAlgorithmParameterException e) {
    throw new IOException(e);
  }
  cipherReset=false;
}
```
Original comment:
```
Calculates the counter and iv, resets the cipher.
```
Generated comment:
```
Reset the chaining variables.
```
---
id345
Code snippet:
```
@SuppressWarnings(\"rawtypes\") public XPathFilterParameterSpec(String xPath,Map namespaceMap){
  if (xPath == null || namespaceMap == null) {
    throw new NullPointerException();
  }
  this.xPath=xPath;
  Map<?,?> copy=new HashMap<>((Map<?,?>)namespaceMap);
  Iterator<? extends Map.Entry<?,?>> entries=copy.entrySet().iterator();
  while (entries.hasNext()) {
    Map.Entry<?,?> me=entries.next();
    if (!(me.getKey() instanceof String) || !(me.getValue() instanceof String)) {
      throw new ClassCastException(\"not a String\");
    }
  }
  @SuppressWarnings(\"unchecked\") Map<String,String> temp=(Map<String,String>)copy;
  nsMap=Collections.unmodifiableMap(temp);
}
```
Original comment:
```
Creates an <code>XPathFilterParameterSpec</code> with the specified XPath expression and namespace map. The map is copied to protect against subsequent modification.
```
Generated comment:
```
Creates a new <code>domnodemap</code> instance.
```
---
id346
Code snippet:
```
public GeneralSecurityException(String msg){
  super(msg);
}
```
Original comment:
```
Constructs a GeneralSecurityException with the specified detail message. A detail message is a String that describes this particular exception.
```
Generated comment:
```
Constructs a new exception with the specified detail message. the cause is not initialized.
```
---
id347
Code snippet:
```
void shutdown(){
synchronized (shutdownLock) {
    shutdown=true;
    shutdownLock.notifyAll();
  }
}
```
Original comment:
```
Call this method to stop the thread. This method is blocking until the thread has stopped.
```
Generated comment:
```
Shutdown the thread pool.
```
---
id348
Code snippet:
```
public void testIntbyInt1(){
  byte aBytes[]={10,20,30,40};
  byte bBytes[]={1,2,3,4};
  int aSign=1;
  int bSign=-1;
  byte rBytes[]={-11,-41,-101,55,5,15,96};
  BigInteger aNumber=new BigInteger(aSign,aBytes);
  BigInteger bNumber=new BigInteger(bSign,bBytes);
  BigInteger result=aNumber.multiply(bNumber);
  byte resBytes[]=new byte[rBytes.length];
  resBytes=result.toByteArray();
  for (int i=0; i < resBytes.length; i++) {
    assertTrue(resBytes[i] == rBytes[i]);
  }
  assertEquals(\"incorrect sign\",-1,result.signum());
}
```
Original comment:
```
Multiply two numbers of 4 bytes length.
```
Generated comment:
```
Multiply a number by zero.
```
---
id349
Code snippet:
```
public void indent(int n) throws SAXException {
}
```
Original comment:
```
Does nothing because  the indent attribute is ignored for text output.
```
Generated comment:
```
Receive notification of character data. <p>the parser will call this method to report each chunk of character data. sax parsers may return all contiguous character data in a single chunk, or they may split it into several chunks; however, all of the characters in any single event must come from the same external entity, so that the locator provides useful information.</p> <p>the application must not attempt to read from the array outside of the specified range.</p>.
```
---
id350
Code snippet:
```
@Override protected void add_to_list(PrintableInfo p_object){
  String curr_filter_string=this.filter_string.getText().trim();
  boolean object_matches;
  if (curr_filter_string.length() == 0) {
    object_matches=true;
  }
 else {
    object_matches=p_object.toString().contains(curr_filter_string);
  }
  if (object_matches) {
    super.add_to_list(p_object);
  }
}
```
Original comment:
```
Adds p_object to the list only if its name matches the filter
```
Generated comment:
```
Adds a filter to the list.
```
---
id351
Code snippet:
```
public void testClose() throws Exception {
  byte[] data=new byte[]{-127,-100,-50,-10,-1,0,1,10,50,127};
  TestOutputStream tos=new TestOutputStream();
  CipherOutputStream cos=new CipherOutputStream(tos){
  }
;
  cos.write(data);
  cos.close();
  byte[] result=tos.toByteArray();
  if (!Arrays.equals(result,data)) {
    fail(\"CipherOutputStream did not flush the data.\");
  }
  assertTrue(\"The close() method should call the close() method \" + \"of its underlying output stream.\",tos.wasClosed());
}
```
Original comment:
```
close() method testing. Tests that the method calls the close() method of the underlying input stream.
```
Generated comment:
```
Java.security.digestoutputstream#write(byte[], int, int).
```
---
id352
Code snippet:
```
private boolean containsBlackPoint(int a,int b,int fixed,boolean horizontal){
  if (horizontal) {
    for (int x=a; x <= b; x++) {
      if (image.get(x,fixed)) {
        return true;
      }
    }
  }
 else {
    for (int y=a; y <= b; y++) {
      if (image.get(fixed,y)) {
        return true;
      }
    }
  }
  return false;
}
```
Original comment:
```
Determines whether a segment contains a black point
```
Generated comment:
```
Returns true if the specified point is contained in this rectangle.
```
---
id353
Code snippet:
```
public static PublicKey generatePublicKey(String encodedPublicKey){
  try {
    byte[] decodedKey=Base64.decode(encodedPublicKey);
    KeyFactory keyFactory=KeyFactory.getInstance(KEY_FACTORY_ALGORITHM);
    return keyFactory.generatePublic(new X509EncodedKeySpec(decodedKey));
  }
 catch (  NoSuchAlgorithmException e) {
    throw new RuntimeException(e);
  }
catch (  InvalidKeySpecException e) {
    Log.e(TAG,\"Invalid key specification.\");
    throw new IllegalArgumentException(e);
  }
catch (  Base64DecoderException e) {
    Log.e(TAG,\"Base64 decoding failed.\");
    throw new IllegalArgumentException(e);
  }
}
```
Original comment:
```
Generates a PublicKey instance from a string containing the Base64-encoded public key.
```
Generated comment:
```
Generates a publickey instance from a string containing the base64-encoded public key.
```
---
id354
Code snippet:
```
static public void assertNotSame(String message,Object expected,Object actual){
  if (expected == actual)   failSame(message);
}
```
Original comment:
```
Asserts that two objects refer to the same object. If they are not an AssertionFailedError is thrown with the given message.
```
Generated comment:
```
Asserts that two objects refer to the same object. if they are not an assertionfailederror is thrown with the given message.
```
---
id355
Code snippet:
```
public SchemaBuilder addToSchemaOverwrite(){
  return getSchemaBuilder().addMatchingRuleUse(new MatchingRuleUse(this),true);
}
```
Original comment:
```
Adds this matching rule use definition to the schema overwriting any existing matching rule use definition with the same numeric OID.
```
Generated comment:
```
Adds a new rule.
```
---
id356
Code snippet:
```
public void mergeDifferent(PdfDictionary other){
  for (  PdfName key : other.keySet()) {
    if (!containsKey(key))     put(key,other.get(key));
  }
}
```
Original comment:
```
This method merges different fields from two dictionaries into the current one
```
Generated comment:
```
Merges the given map with the given map.
```
---
id357
Code snippet:
```
public Builder removeRequiredAttribute(final String nameOrOID){
  this.requiredAttributes.remove(nameOrOID);
  return this;
}
```
Original comment:
```
Removes the specified required attribute.
```
Generated comment:
```
Removes an attribute with the given name.
```
---
id358
Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList elementList;
  Element testNode;
  boolean state;
  doc=(Document)load(\"staffNS\",false);
  elementList=doc.getElementsByTagName(\"address\");
  testNode=(Element)elementList.item(0);
  state=testNode.hasAttribute(\"dmstc:domestic\");
  assertTrue(\"hasDomesticAttr\",state);
}
```
Original comment:
```
Runs the test case.
```
Generated comment:
```
Runs the test case.
```
---
id359
Code snippet:
```
public Name(byte[] encoding) throws IOException {
  DerInputStream in=new DerInputStream(encoding);
  if (in.getEndOffset() != encoding.length) {
    throw new IOException(\"Wrong content length\");
  }
  ASN1.decode(in);
  this.rdn=(List<List<AttributeTypeAndValue>>)in.content;
}
```
Original comment:
```
Creates new <code>Name</code> instance from its DER encoding
```
Generated comment:
```
Creates the extension object on the base of its encoded form.
```
---
id360
Code snippet:
```
private LdapException interrupted(InterruptedException e){
  return newLdapException(ResultCode.CLIENT_SIDE_USER_CANCELLED,e);
}
```
Original comment:
```
Handle thread interruption.
```
Generated comment:
```
Returns a cached instance if such is available or a new one is instantiated.
```
---
id361
Code snippet:
```
public DERSequence(ASN1Encodable[] array){
  super(array);
}
```
Original comment:
```
create a sequence containing an array of objects.
```
Generated comment:
```
Create a sequence containing an array of objects.
```
---
id362
Code snippet:
```
public static Request parseXML(String xml) throws SAMLException {
  Document doc=XMLUtils.toDOMDocument(xml,SAMLUtils.debug);
  Element root=doc.getDocumentElement();
  return new Request(root);
}
```
Original comment:
```
This method shall only be used at the server side to reconstruct a Request object based on the XML document received from client. The schema of this XML document is described above.
```
Generated comment:
```
Parses an element of the specified type.
```
---
id363
Code snippet:
```
public XObject execute(XPathContext xctxt) throws javax.xml.transform.TransformerException {
  XObject expr1=m_left.execute(xctxt);
  if (expr1.bool()) {
    XObject expr2=m_right.execute(xctxt);
    return expr2.bool() ? XBoolean.S_TRUE : XBoolean.S_FALSE;
  }
 else   return XBoolean.S_FALSE;
}
```
Original comment:
```
AND two expressions and return the boolean result. Override superclass method for optimization purposes.
```
Generated comment:
```
Execute the function. the function must return a valid object.
```
---
id364
Code snippet:
```
public Segment(){
  this(null,0,0);
}
```
Original comment:
```
Creates a new segment.
```
Generated comment:
```
Creates a new segment.
```
---
id365
Code snippet:
```
public int append(ByteBuffer data,int len,boolean count){
  buffer.append(data,len);
  int pkgCnt=-1;
  if (count)   pkgCnt=buffer.countPackages();
  return pkgCnt;
}
```
Original comment:
```
Append new bytes to buffer.
```
Generated comment:
```
Appends the specified byte to this byte buffer.
```
---
id366
Code snippet:
```
public void updateDeltas(int deltaX,int deltaY){
  if (mLeftBorderActive) {
    mDeltaX=Math.max(-mBaselineX,deltaX);
    mDeltaX=Math.min(mBaselineWidth - 2 * mTouchTargetWidth,mDeltaX);
  }
 else   if (mRightBorderActive) {
    mDeltaX=Math.min(mDragLayer.getWidth() - (mBaselineX + mBaselineWidth),deltaX);
    mDeltaX=Math.max(-mBaselineWidth + 2 * mTouchTargetWidth,mDeltaX);
  }
  if (mTopBorderActive) {
    mDeltaY=Math.max(-mBaselineY,deltaY);
    mDeltaY=Math.min(mBaselineHeight - 2 * mTouchTargetWidth,mDeltaY);
  }
 else   if (mBottomBorderActive) {
    mDeltaY=Math.min(mDragLayer.getHeight() - (mBaselineY + mBaselineHeight),deltaY);
    mDeltaY=Math.max(-mBaselineHeight + 2 * mTouchTargetWidth,mDeltaY);
  }
}
```
Original comment:
```
Here we bound the deltas such that the frame cannot be stretched beyond the extents of the CellLayout, and such that the frame\'s borders can\'t cross.
```
Generated comment:
```
Update the size of the drawable.
```
---
id367
Code snippet:
```
public SerializablePermission(String name,String actions){
  super(name,actions);
}
```
Original comment:
```
Creates a new SerializablePermission object with the specified name. The name is the symbolic name of the SerializablePermission, and the actions String is currently unused and should be null.
```
Generated comment:
```
Constructs a new exception with the specified detail message. the cause is not initialized.
```
---
id368
Code snippet:
```
void processDragOver(DragSourceDragEvent dsde){
  DragSourceListener dsl=listener;
  if (dsl != null) {
    dsl.dragOver(dsde);
  }
}
```
Original comment:
```
This method calls <code>dragOver</code> on the <code>DragSourceListener</code>s registered with this <code>DragSource</code>, and passes them the specified <code>DragSourceDragEvent</code>.
```
Generated comment:
```
Does nothing.
```
---
id369
Code snippet:
```
public void transform(Source xmlSource,Result outputTarget,boolean shouldRelease) throws TransformerException {
synchronized (m_reentryGuard) {
    SerializationHandler xoh=createSerializationHandler(outputTarget);
    this.setSerializationHandler(xoh);
    m_outputTarget=outputTarget;
    transform(xmlSource,shouldRelease);
  }
}
```
Original comment:
```
Process the source tree to the output result.
```
Generated comment:
```
This method is called when a new xml element is encountered.
```
---
id370
Code snippet:
```
@SuppressWarnings(\"unchecked\") private E removeAt(int i){
  modCount++;
  int s=--size;
  if (s == i)   queue[i]=null;
 else {
    E moved=(E)queue[s];
    queue[s]=null;
    siftDown(i,moved);
    if (queue[i] == moved) {
      siftUp(i,moved);
      if (queue[i] != moved)       return moved;
    }
  }
  return null;
}
```
Original comment:
```
Removes the ith element from queue. Normally this method leaves the elements at up to i-1, inclusive, untouched.  Under these circumstances, it returns null.  Occasionally, in order to maintain the heap invariant, it must swap a later element of the list with one earlier than i.  Under these circumstances, this method returns the element that was previously at the end of the list and is now at some position before i. This fact is used by iterator.remove so as to avoid missing traversing elements.
```
Generated comment:
```
Removes the element at the specified position in this list. shifts any subsequent elements to the left (subtracts one from their indices). returns the element that was removed from the list.
```
---
id371
Code snippet:
```
public LogException(){
  super();
}
```
Original comment:
```
Constructs a log exception.
```
Generated comment:
```
Constructs a new exception with <code>null</code> as its detail message. the cause is not initialized.
```
---
id372
Code snippet:
```
public static Charset forName(String charsetName){
  return forName(charsetName,null);
}
```
Original comment:
```
Safely gets charset for the specified name
```
Generated comment:
```
Returns the charset specified in the content-type of this header, or the http default (iso-8859-1) if none can be found.
```
---
id373
Code snippet:
```
@Override protected boolean checkParam(final String reqParam) throws ConnectorException {
  if (reqParam == null || reqParam.equals(\"\")) {
    return true;
  }
  if (Pattern.compile(Constants.INVALID_PATH_REGEX).matcher(reqParam).find()) {
    return false;
  }
  return true;
}
```
Original comment:
```
for error command there should be no exection throw becouse there is no more excetpion handlers.
```
Generated comment:
```
Checks if the given string is a valid string.
```
---
id374
Code snippet:
```
@Override public void recycle(){
  input=null;
}
```
Original comment:
```
Make the filter ready to process the next request.
```
Generated comment:
```
Recycles the object.
```
---
id375
Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList elementList;
  Element testAddr;
  Node textNode;
  int nodeType;
  doc=(Document)load(\"staff\",false);
  elementList=doc.getElementsByTagName(\"address\");
  testAddr=(Element)elementList.item(0);
  textNode=testAddr.getFirstChild();
  nodeType=(int)textNode.getNodeType();
  assertEquals(\"nodeTextNodeTypeAssert1\",3,nodeType);
}
```
Original comment:
```
Runs the test case.
```
Generated comment:
```
Runs the test case.
```
---
id376
Code snippet:
```
public Cursor fetch(Long ruleActionID){
  if (ruleActionID == null) {
    throw new IllegalArgumentException(\"primary key null.\");
  }
  Cursor mCursor=database.query(true,DATABASE_TABLE,KEYS,KEY_RULEACTIONID + \"=\" + ruleActionID,null,null,null,null,null);
  if (mCursor != null) {
    mCursor.moveToFirst();
  }
  return mCursor;
}
```
Original comment:
```
Return a Cursor pointing to the record matches the ruleActionID.
```
Generated comment:
```
Fetch a cursor from the cursor.
```
---
id377
Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  Element elementNode;
  String elementName;
  doc=(Document)load(\"hc_staff\",false);
  elementNode=doc.getDocumentElement();
  elementName=elementNode.getNodeName();
  if ((\"image/svg+xml\".equals(getContentType()))) {
    assertEquals(\"svgNodeName\",\"svg\",elementName);
  }
 else {
    assertEqualsAutoCase(\"element\",\"nodeName\",\"html\",elementName);
  }
}
```
Original comment:
```
Runs the test case.
```
Generated comment:
```
Runs the test case.
```
---
id378
Code snippet:
```
private boolean isLoginFailureLockoutMode(){
  return loginFailureLockoutMode;
}
```
Original comment:
```
Indicates accountlocking mode is enabled.
```
Generated comment:
```
Gets the value of the locked property.
```
---
id379
Code snippet:
```
private int success(Assertion assertion,NameID nameId,String userName) throws AuthLoginException, SAML2Exception {
  setSessionProperties(assertion,nameId,userName);
  setSessionAttributes(assertion,userName);
  DEBUG.message(\"SAML2 :: User Authenticated via SAML2 - {}\",getPrincipal().getName());
  storeUsernamePasswd(DNUtils.DNtoName(getPrincipal().getName()),null);
  return ISAuthConstants.LOGIN_SUCCEED;
}
```
Original comment:
```
Sets the auth module\'s logged-in username via storeUsernamePasswd, triggers call to add information necessary for SLO (if configured) and returns success.
```
Generated comment:
```
Creates a new user.
```
---
id380
Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(hc_nodegetownerdocumentnull.class,args);
}
```
Original comment:
```
Runs this test from the command line.
```
Generated comment:
```
Runs this test from the command line.
```
---
id381
Code snippet:
```
public void write(char cbuf[],int off,int len) throws IOException {
  se.write(cbuf,off,len);
}
```
Original comment:
```
Writes a portion of an array of characters.
```
Generated comment:
```
Write a portion of an array of characters.
```
---
id382
Code snippet:
```
private UnicodeBlock(String idName){
  super(idName);
  map.put(idName,this);
}
```
Original comment:
```
Creates a UnicodeBlock with the given identifier name. This name must be the same as the block identifier.
```
Generated comment:
```
Creates a new instance.
```
---
id383
Code snippet:
```
public static void copy(String input,OutputStream output) throws IOException {
  StringReader in=new StringReader(input);
  OutputStreamWriter out=new OutputStreamWriter(output);
  copy(in,out);
  out.flush();
}
```
Original comment:
```
Serialize chars from a <code>String</code> to bytes on an <code>OutputStream</code>, and flush the <code>OutputStream</code>.
```
Generated comment:
```
Copy the contents of the given inputstream to the given outputstream. closes both when done.
```
---
id384
Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(hc_textwithnomarkup.class,args);
}
```
Original comment:
```
Runs this test from the command line.
```
Generated comment:
```
Runs this test from the command line.
```
---
id385
Code snippet:
```
@Override public boolean accept(File file){
  String name=file.getName();
  for (  String wildcard : wildcards) {
    if (FilenameUtils.wildcardMatch(name,wildcard,caseSensitivity)) {
      return true;
    }
  }
  return false;
}
```
Original comment:
```
Checks to see if the filename matches one of the wildcards.
```
Generated comment:
```
Returns true if the file is a file.
```
---
id386
Code snippet:
```
@Deprecated public ServerRuntimeException(String s,Exception ex){
  super(s,ex);
}
```
Original comment:
```
Constructs a <code>ServerRuntimeException</code> with the specified detail message and nested exception.
```
Generated comment:
```
Constructs a new instance with the specified detail message. the cause is not initialized.
```
---
id387
Code snippet:
```
public IOException(Throwable cause){
  super(cause == null ? null : cause.toString(),cause);
}
```
Original comment:
```
Constructs a new instance of this class with its detail cause filled in.
```
Generated comment:
```
Constructs a new instance with the given cause.
```
---
id388
Code snippet:
```
protected void addMissingNamespaces(final JKTagWrapper wrapper){
  final JKFacesConfigurations config=JKFacesConfigurations.getInstance();
  final List<JKNamespace> namespaces=config.getNamespaces();
  for (  final JKNamespace namespace : namespaces) {
    wrapper.addAttribue(namespace.getPrefix(),namespace.getUrl());
  }
}
```
Original comment:
```
Adds the names spaces.
```
Generated comment:
```
Adds a new namespace to the list of namespaces.
```
---
id389
Code snippet:
```
public void runTest() throws Throwable {
  String publicId=\"http://www.example.com/\";
  String systemId=\"myDoc.dtd\";
  String qualifiedName;
  DocumentType docType=null;
  DOMImplementation domImpl;
  domImpl=getImplementation();
{
    boolean success=false;
    try {
      docType=domImpl.createDocumentType(\"\",publicId,systemId);
    }
 catch (    DOMException ex) {
      success=(ex.code == DOMException.INVALID_CHARACTER_ERR);
    }
    assertTrue(\"throw_INVALID_CHARACTER_ERR\",success);
  }
}
```
Original comment:
```
Runs the test case.
```
Generated comment:
```
Runs the test case.
```
---
id390
Code snippet:
```
public static boolean isStrikeThrough(AttributeSet a){
  Boolean strike=(Boolean)a.getAttribute(StrikeThrough);
  if (strike != null) {
    return strike.booleanValue();
  }
  return false;
}
```
Original comment:
```
Checks whether the strikethrough attribute is set.
```
Generated comment:
```
Returns true if the given attribute is set.
```
---
id391
Code snippet:
```
@Override public Node insertChildAt(Node toInsert,int index){
  if (toInsert instanceof Element && getDocumentElement() != null) {
    throw new DOMException(DOMException.HIERARCHY_REQUEST_ERR,\"Only one root element allowed\");
  }
  if (toInsert instanceof DocumentType && getDoctype() != null) {
    throw new DOMException(DOMException.HIERARCHY_REQUEST_ERR,\"Only one DOCTYPE element allowed\");
  }
  return super.insertChildAt(toInsert,index);
}
```
Original comment:
```
Document elements may have at most one root element and at most one DTD element.
```
Generated comment:
```
Inserts the specified element into this vector at the specified index. each component in this vector with an index greater or equal to the specified index is shifted downward to have an index one greater than the value it had previously.
```
---
id392
Code snippet:
```
public static <T>boolean remove(Collection<T> collection,T element){
  if (element == null) {
    return false;
  }
  if (CollectionUtils.isEmpty(collection)) {
    return false;
  }
  return collection.remove(element);
}
```
Original comment:
```
Safe method to remove an element from collection. If either collection is empty or element is null - returns false.
```
Generated comment:
```
Removes all elements in the specified collection that are not contained in the specified collection.
```
---
id393
Code snippet:
```
public void put(String uri) throws IOException {
  put(uri,null,null);
}
```
Original comment:
```
Put to URI
```
Generated comment:
```
Adds a uri to the request.
```
---
id394
Code snippet:
```
public static PublicKeySelector fromString(String type){
  if (type != null) {
    for (    PublicKeySelector keySelector : PublicKeySelector.values()) {
      if (type.equalsIgnoreCase(keySelector.type)) {
        return keySelector;
      }
    }
  }
  return null;
}
```
Original comment:
```
Translates a string into a token endpoint auth method type.
```
Generated comment:
```
Creates a new <code>keymap</code> instance.
```
---
id395
Code snippet:
```
private String normalizeHost(String host){
  if (LOCALHOST.equals(host)) {
    return LOCALHOST;
  }
  try {
    final InetAddress inetAddress=InetAddress.getByName(host);
    if (isLocalAddress(inetAddress)) {
      return LOCALHOST;
    }
    return inetAddress.getHostAddress();
  }
 catch (  UnknownHostException e) {
    logger.error(ERR_COULD_NOT_SOLVE_HOSTNAME,host);
    return host;
  }
}
```
Original comment:
```
Returns a normalized String representation of the supplied host.
```
Generated comment:
```
Normalizes the host name.
```
---
id396
Code snippet:
```
public void schemaChanged(String serviceName,String version){
}
```
Original comment:
```
This method will be invoked when a service\'s schema has been changed.
```
Generated comment:
```
This method was generated by mybatis generator. this method corresponds to the database table company.
```
---
id397
Code snippet:
```
public AMAccessAuditEventBuilder requestDetail(JsonValue detail){
  return addDetail(detail,REQUEST);
}
```
Original comment:
```
Adds a JSON object of detail for the request.
```
Generated comment:
```
Adds a new event.
```
---
id398
Code snippet:
```
public CompareOperationBasis(ClientConnection clientConnection,long operationID,int messageID,List<Control> requestControls,ByteString rawEntryDN,String rawAttributeType,ByteString assertionValue){
  super(clientConnection,operationID,messageID,requestControls);
  this.rawEntryDN=rawEntryDN;
  this.rawAttributeType=rawAttributeType;
  this.assertionValue=assertionValue;
  responseControls=new ArrayList<>();
  entryDN=null;
  attributeDescription=null;
  cancelRequest=null;
  proxiedAuthorizationDN=null;
}
```
Original comment:
```
Creates a new compare operation with the provided information.
```
Generated comment:
```
Creates a new alert.
```
---
id399
Code snippet:
```
public SAML2ResponseData(){
}
```
Original comment:
```
Dummy creator, used by databinder to generate this POJO.
```
Generated comment:
```
Creates a new instance.
```
---
id400
Code snippet:
```
public void cutout_traces(Collection<BrdItem> p_item_list){
  for (  BrdItem curr_item : p_item_list) {
    if (!(curr_item instanceof BrdTracep))     continue;
    BrdTracep a_trace=(BrdTracep)curr_item;
    if (a_trace.shares_net_no(own_net_nos))     continue;
    cutout_trace(a_trace,shape,cl_class);
  }
}
```
Original comment:
```
Cuts out all traces in p_item_list out of the stored shape.  Traces with net number p_except_net_no are ignored
```
Generated comment:
```
This method is used to fixup variables from qnames to stack frame indexes at stylesheet build time.
```
---
id401
Code snippet:
```
private SOAPMessage FormSOAPError(String faultCode,Throwable throwable,Message req){
  String faultString=throwable.getMessage();
  if (faultString == null || faultString.length() == 0) {
    faultString=Utils.bundle.getString(\"unknownError\");
  }
  return FormSOAPError(req,faultCode,faultString);
}
```
Original comment:
```
Constructs a SOAPMessage with specified fault code and Throwable. The fault string will be Throwable.getMessage(); The fault code will have same namespace of soap envelope.
```
Generated comment:
```
Send an error log message.
```
---
id402
Code snippet:
```
private static int removeWhiteSpace(char[] data){
  if (data == null) {
    return 0;
  }
  int newSize=0;
  int len=data.length;
  for (int i=0; i < len; i++) {
    if (!isWhiteSpace(data[i])) {
      data[newSize++]=data[i];
    }
  }
  return newSize;
}
```
Original comment:
```
remove WhiteSpace from MIME containing encoded Base64 data.
```
Generated comment:
```
Remove whitespace from mime containing encoded base64 data.
```
---
id403
Code snippet:
```
public static void removeByField2(boolean field2){
  getPersistence().removeByField2(field2);
}
```
Original comment:
```
Removes all the foos where field2 = &#63; from the database.
```
Generated comment:
```
Removes the specified field from the constant pool of the class being build. does nothing if the constant pool already contains a similar item.
```
---
id404
Code snippet:
```
public List<VerificationOK> verify(List<VerificationOK> result) throws IOException, GeneralSecurityException {
  if (result == null)   result=new ArrayList<>();
  while (pkcs7 != null) {
    result.addAll(verifySignature());
  }
  return result;
}
```
Original comment:
```
Verifies all the document-level timestamps and all the signatures in the document.
```
Generated comment:
```
This method verifies that the given argument is not null.
```
---
id405
Code snippet:
```
protected Set separateAdditionalProperties(Map m){
  Set addProps=null;
  if ((m != null) && ((addProps=(Set)m.get(ADD_PROP_ATTR)) != null) && (addProps.size() > 0)) {
    m.remove(ADD_PROP_ATTR);
    Iterator itr=addProps.iterator();
    while (itr.hasNext()) {
      String property=(String)itr.next();
      int index=property.indexOf(SEPARATOR);
      if (index <= 0) {
        continue;
      }
      String name=property.substring(0,index);
      String val=property.substring(index + 1);
      Set set=new HashSet(1);
      set.add(val);
      m.put(name,set);
    }
  }
  return addProps;
}
```
Original comment:
```
Removes the \"additionalProperties\" element from the Map, adds each of them to the Map with name and value (parsed with \"=\") and returns the values of the \"additionalProperties in the Set.
```
Generated comment:
```
Add a property to the list.
```
---
id406
Code snippet:
```
public synchronized void ensureRestExpressRunning() throws IOException, IllegalAccessException, InstantiationException {
  ensureRestExpressRunning(true);
}
```
Original comment:
```
Ensures RestExpress is presently running. Cassandra will be mocked instead of relying on a external process.
```
Generated comment:
```
Ensures that the stream is not closed.
```
---
id407
Code snippet:
```
public com.sun.identity.liberty.ws.common.jaxb.utility.TimestampElement createTimestampElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.liberty.ws.common.jaxb.utility.impl.TimestampElementImpl();
}
```
Original comment:
```
Create an instance of TimestampElement
```
Generated comment:
```
Returns a new element with the given element as its parent.
```
---
id408
Code snippet:
```
public static boolean isPrivilegedPort(int port){
  return SetupUtils.isPrivilegedPort(port);
}
```
Original comment:
```
Returns whether the provided port is a privileged port.
```
Generated comment:
```
Returns the port number.
```
---
id409
Code snippet:
```
public UserAttributeNotificationMessageTemplateElement(AttributeType attributeType){
  this.attributeType=attributeType;
}
```
Original comment:
```
Creates a new user DN notification message template element.
```
Generated comment:
```
Constructs a new exception with the specified detail message. the cause is not initialized.
```
---
id410
Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  DOMImplementation domImpl;
  boolean state;
  doc=(Document)load(\"hc_staff\",false);
  domImpl=doc.getImplementation();
  if ((\"text/html\".equals(getContentType()))) {
    state=domImpl.hasFeature(\"html\",\"1.0\");
    assertTrue(\"supports_html_1.0\",state);
  }
 else {
    state=domImpl.hasFeature(\"xml\",\"1.0\");
    assertTrue(\"supports_xml_1.0\",state);
  }
}
```
Original comment:
```
Runs the test case.
```
Generated comment:
```
Runs the test case.
```
---
id411
Code snippet:
```
public void windowDeactivated(WindowEvent e){
  ((WindowListener)a).windowDeactivated(e);
  ((WindowListener)b).windowDeactivated(e);
}
```
Original comment:
```
Handles the windowDeactivated event by invoking the windowDeactivated methods on listener-a and listener-b.
```
Generated comment:
```
Called when a window is activated.
```
---
id412
Code snippet:
```
public static void deregisterAlertHandler(AlertHandler<?> alertHandler){
  directoryServer.alertHandlers.remove(alertHandler);
}
```
Original comment:
```
Deregisters the provided alert handler with the Directory Server.
```
Generated comment:
```
Removes a client from the server.
```
---
id413
Code snippet:
```
public JsonValue notifyUpdate(Context context,String resourceContainer,String resourceId,JsonValue oldValue,JsonValue newValue) throws SynchronizationException {
  if (isSourceObject(resourceContainer,resourceId)) {
    if (newValue == null || newValue.getObject() == null) {
      newValue=LazyObjectAccessor.rawReadObject(connectionFactory,context,resourceContainer,resourceId);
    }
    if (oldValue == null || oldValue.getObject() == null || !oldValue.isEqualTo(newValue)) {
      return doSourceSync(context,resourceId,newValue,false,oldValue);
    }
 else {
      LOGGER.trace(\"There is nothing to update on {}\",resourceContainer + \"/\" + resourceId);
    }
  }
  return json(null);
}
```
Original comment:
```
Notify the target system that an object has been updated in a source system.
```
Generated comment:
```
Notify all registered listeners of the specified type.
```
---
id414
Code snippet:
```
public int compareTo(BrdTraceInfo p_other){
  return p_other.layer - layer;
}
```
Original comment:
```
Implements the comparable interface.
```
Generated comment:
```
Compares two objects.
```
---
id415
Code snippet:
```
public Hashtable(){
  this(11,0.75f);
}
```
Original comment:
```
Constructs a new, empty hashtable with a default initial capacity (11) and load factor (0.75).
```
Generated comment:
```
Constructs a new, empty hashtable.
```
---
id416
Code snippet:
```
public Builder ruleID(final int ruleID){
  this.ruleID=ruleID;
  return this;
}
```
Original comment:
```
Sets the the numeric ID which uniquely identifies this structure rule.
```
Generated comment:
```
Sets the maximum number of characters in the builder.
```
---
id417
Code snippet:
```
private static void extractFileFromZip(ZipInputStream zipInput,File targetFile) throws IOException {
  try (BufferedOutputStream outputStream=new BufferedOutputStream(new FileOutputStream(targetFile))){
    int bytesRead=0;
    byte[] bytes=new byte[BUFFER_SIZE];
    while ((bytesRead=zipInput.read(bytes)) != -1) {
      outputStream.write(bytes,0,bytesRead);
    }
  }
 }
```
Original comment:
```
Extracts a file from a zip input stream.
```
Generated comment:
```
Read a file.
```
---
id418
Code snippet:
```
public static boolean match(String name){
  if (osName.equalsIgnoreCase(name)) {
    return true;
  }
 else {
    String winPrefix=name.substring(0,3);
    if (osName.toLowerCase().contains(winPrefix.toLowerCase())) {
      return true;
    }
  }
  return false;
}
```
Original comment:
```
check if operating system matches with a given operating system name  <br>
```
Generated comment:
```
Returns true if the given string is a valid name according to [7] in the xml 1.0 recommendation.
```
---
id419
Code snippet:
```
public BeanContextSupport(BeanContext peer,Locale lcle,boolean dTime,boolean visible){
  super(peer);
  locale=lcle != null ? lcle : Locale.getDefault();
  designTime=dTime;
  okToUseGui=visible;
  initialize();
}
```
Original comment:
```
Construct a BeanContextSupport instance
```
Generated comment:
```
Creates a new instance.
```
---
id420
Code snippet:
```
public void repaint(long tm,int x,int y,int width,int height){
  RepaintManager.currentManager(SunToolkit.targetToAppContext(this)).addDirtyRegion(this,x,y,width,height);
}
```
Original comment:
```
Adds the specified region to the dirty region list if the component is showing.  The component will be repainted after all of the currently pending events have been dispatched.
```
Generated comment:
```
Overridden for performance reasons. see the <a href=\"#override\">implementation note</a> for more information.
```
---
id421
Code snippet:
```
@Override public boolean equals(Object o){
  rwlock.readLock().lock();
  try {
    if (o == this) {
      return true;
    }
    if (!(o instanceof Map)) {
      return false;
    }
    Map t=(Map)o;
    if (t.size() != size()) {
      return false;
    }
    for (Iterator i=entrySet().iterator(); i.hasNext(); ) {
      Entry e=(Entry)i.next();
      Object key=e.getKey();
      Object value=e.getValue();
      if (value == null) {
        if (!(t.get(key) == null && t.containsKey(key))) {
          return false;
        }
      }
 else {
        if (!value.equals(t.get(key))) {
          return false;
        }
      }
    }
    return true;
  }
  finally {
    rwlock.readLock().unlock();
  }
}
```
Original comment:
```
Compares the specified Object with this Map for equality, as per the definition in the Map interface.
```
Generated comment:
```
Compares this map with another map for equality of their stored entries.
```
---
id422
Code snippet:
```
public RecoveryCodeGenerator(SecureRandom secureRandom,int retryMaximum){
  this.secureRandom=secureRandom;
  this.retryMaximum=retryMaximum;
}
```
Original comment:
```
Generates a new CodeUtils which can be used to generate a plethora of codes suited to fit your needs.
```
Generated comment:
```
Constructs a new retry policy.
```
---
id423
Code snippet:
```
public ImageWriteParam(Locale locale){
  this.locale=locale;
}
```
Original comment:
```
Constructs an <code>ImageWriteParam</code> set to use a given <code>Locale</code>.
```
Generated comment:
```
Creates a new image store.
```
---
id424
Code snippet:
```
void saveDeviceProfile(@Nonnull String user,@Nonnull String realm,@Nonnull OathDeviceSettings deviceSettings) throws AuthLoginException {
  Reject.ifNull(user,realm,deviceSettings);
  try {
    devicesDao.saveDeviceProfiles(user,realm,jsonUtils.toJsonValues(Collections.singletonList(deviceSettings)));
  }
 catch (  IOException e) {
    debug.error(\"OathMaker.createDeviceProfile(): Unable to save device profile for user {} in realm {}\",user,realm,e);
    throw new AuthLoginException(e);
  }
}
```
Original comment:
```
Saves the OATH device settings to the user\'s profile, overwriting any existing device profile.
```
Generated comment:
```
Saves the device profile to the database.
```
---
id425
Code snippet:
```
public void addAttribute(String rawName,String value){
  if (m_firstTagNotEmitted) {
    flush();
  }
  m_handler.addAttribute(rawName,value);
}
```
Original comment:
```
Adds an attribute to the currenly open tag
```
Generated comment:
```
Adds an attribute to the end of the list.
```
---
id426
Code snippet:
```
public boolean isDouble(STypeDef requiredType,LineCol lineCol) throws SyntaxException {
  return (requiredType == null || requiredType instanceof DoubleTypeDef || requiredType instanceof SClassDef && requiredType.isAssignableFrom(getTypeWithName(\"java.lang.Double\",lineCol)));
}
```
Original comment:
```
check whether the required type is double type<br> number literal always will match double value
```
Generated comment:
```
Returns true if the given type is assignable from the given type.
```
---
id427
Code snippet:
```
public DefaultHandler2(){
}
```
Original comment:
```
Constructs a handler which ignores all parsing events.
```
Generated comment:
```
Creates a new instance.
```
---
id428
Code snippet:
```
@Override public byte[] wrap(final byte[] outgoing,final int offset,final int len) throws LdapException {
  final byte[] copy=new byte[len];
  System.arraycopy(outgoing,offset,copy,0,len);
  return copy;
}
```
Original comment:
```
Default implementation just returns the copy of the bytes.
```
Generated comment:
```
Unwraps a byte array.
```
---
id429
Code snippet:
```
public Attributes(Attributes attr){
  map=new HashMap<>(attr);
}
```
Original comment:
```
Constructs a new Attributes object with the same attribute name-value mappings as in the specified Attributes.
```
Generated comment:
```
Constructs a copy of the given attribute.
```
---
id430
Code snippet:
```
public CompareOperationBasis(ClientConnection clientConnection,long operationID,int messageID,List<Control> requestControls,DN entryDN,AttributeDescription attributeDescription,ByteString assertionValue){
  super(clientConnection,operationID,messageID,requestControls);
  this.entryDN=entryDN;
  this.attributeDescription=attributeDescription;
  this.assertionValue=assertionValue;
  responseControls=new ArrayList<>();
  rawEntryDN=ByteString.valueOfUtf8(entryDN.toString());
  rawAttributeType=attributeDescription.toString();
  cancelRequest=null;
  proxiedAuthorizationDN=null;
}
```
Original comment:
```
Creates a new compare operation with the provided information.
```
Generated comment:
```
Creates a new instance.
```
---
id431
Code snippet:
```
public FrameBodyTOLY(byte textEncoding,String text){
  super(textEncoding,text);
}
```
Original comment:
```
Creates a new FrameBodyTOLY datatype.
```
Generated comment:
```
Creates a new <code>tinputstream</code> instance.
```
---
id432
Code snippet:
```
public static byte[] hexStringToByteArray(String hexString){
  int read=hexString.length();
  byte[] byteArray=new byte[read / 2];
  for (int i=0, j=0; i < read; i++, j++) {
    String part=hexString.substring(i,i + 2);
    byteArray[j]=new Short(Integer.toString(Integer.parseInt(part,16))).byteValue();
    i++;
  }
  return byteArray;
}
```
Original comment:
```
Converts a HEX encoded string to a byte array.
```
Generated comment:
```
Convert a string to a byte array.
```
---
id433
Code snippet:
```
public boolean isSource(){
  return isSource;
}
```
Original comment:
```
Indicates whether the port is a source or a target for its mixer.
```
Generated comment:
```
Returns <code>true</code>.
```
---
id434
Code snippet:
```
private void readObject(ObjectInputStream s) throws ClassNotFoundException, IOException, HeadlessException {
  GraphicsEnvironment.checkHeadless();
  s.defaultReadObject();
  this.text=(text != null) ? text : \"\";
  select(selectionStart,selectionEnd);
  Object keyOrNull;
  while (null != (keyOrNull=s.readObject())) {
    String key=((String)keyOrNull).intern();
    if (textListenerK == key) {
      addTextListener((TextListener)(s.readObject()));
    }
 else {
      s.readObject();
    }
  }
  enableInputMethodsIfNecessary();
}
```
Original comment:
```
Read the ObjectInputStream, and if it isn\'t null, add a listener to receive text events fired by the TextComponent.  Unrecognized keys or values will be ignored.
```
Generated comment:
```
Provides serialization support.
```
---
id435
Code snippet:
```
public MarshalException(Throwable cause){
  super(cause == null ? null : cause.toString());
  this.cause=cause;
}
```
Original comment:
```
Constructs a new <code>MarshalException</code> with the specified cause and a detail message of <code>(cause==null ? null : cause.toString()) </code> (which typically contains the class and detail message of <code>cause</code>).
```
Generated comment:
```
Constructs a new instance with the given cause.
```
---
id436
Code snippet:
```
@Override public String toString(){
  return buf.toString();
}
```
Original comment:
```
Returns the signature that was built by this signature writer.
```
Generated comment:
```
Returns a string representation of this object.
```
---
id437
Code snippet:
```
public SearchResults(int count,Set<T> results,int errorCode){
  this.count=count;
  searchResults=results;
  this.errorCode=errorCode;
}
```
Original comment:
```
Constructs the <code>SearchResults</code> object.
```
Generated comment:
```
Constructs a new exception with the specified detail message. the cause is not initialized.
```
---
id438
Code snippet:
```
private static void initStatics(){
  aciType=getSchema().getAttributeType(\"aci\");
  globalAciType=getSchema().getAttributeType(ATTR_AUTHZ_GLOBAL_ACI);
  debugSearchIndex=getSchema().getAttributeType(SuffixContainer.ATTR_DEBUG_SEARCH_INDEX);
  refAttrType=getSchema().getAttributeType(ATTR_REFERRAL_URL);
  try {
    debugSearchIndexDN=DN.valueOf(\"cn=debugsearch\");
  }
 catch (  LocalizedIllegalArgumentException unexpected) {
  }
}
```
Original comment:
```
We initialize these for each new AciHandler so that we can clear out the stale references that can occur during an in-core restart.
```
Generated comment:
```
Init methods.
```
---
id439
Code snippet:
```
public void mouseExited(MouseEvent e){
  if (e.getSource() == BasicSplitPaneDivider.this) {
    setMouseOver(false);
  }
}
```
Original comment:
```
Invoked when the mouse exits a component.
```
Generated comment:
```
Mouse listener.
```
---
id440
Code snippet:
```
public static String buildStateKey(int taskId,String key){
  return prefixState(taskId) + key;
}
```
Original comment:
```
Build state key to store state value into redis
```
Generated comment:
```
Build a key for the given key.
```
---
id441
Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  Document aNewDoc;
  Element element;
  Node aNode;
  boolean hasChild;
  Document ownerDocument;
  DocumentType docType;
  String system;
  String name;
  NodeList addresses;
  doc=(Document)load(\"staffNS\",true);
  aNewDoc=(Document)load(\"staffNS\",true);
  addresses=aNewDoc.getElementsByTagName(\"emp:address\");
  element=(Element)addresses.item(0);
  assertNotNull(\"empAddressNotNull\",element);
  aNode=doc.importNode(element,false);
  hasChild=aNode.hasChildNodes();
  assertFalse(\"hasChild\",hasChild);
  ownerDocument=aNode.getOwnerDocument();
  docType=ownerDocument.getDoctype();
  system=docType.getSystemId();
  assertURIEquals(\"dtdSystemId\",null,null,null,\"staffNS.dtd\",null,null,null,null,system);
  name=aNode.getNodeName();
  assertEquals(\"nodeName\",\"emp:address\",name);
}
```
Original comment:
```
Runs the test case.
```
Generated comment:
```
Runs the test case.
```
---
id442
Code snippet:
```
public Chunk(final GUID headerGuid,final BigInteger chunkLen){
  if (headerGuid == null) {
    throw new IllegalArgumentException(\"GUID must not be null.\");
  }
  if (chunkLen == null || chunkLen.compareTo(BigInteger.ZERO) < 0) {
    throw new IllegalArgumentException(\"chunkLen must not be null nor negative.\");
  }
  this.guid=headerGuid;
  this.chunkLength=chunkLen;
}
```
Original comment:
```
Creates an instance
```
Generated comment:
```
Creates a new <code>biginteger</code> instance.
```
---
id443
Code snippet:
```
public com.sun.identity.liberty.ws.disco.jaxb.ServiceTypeElement createServiceTypeElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.liberty.ws.disco.jaxb.impl.ServiceTypeElementImpl();
}
```
Original comment:
```
Create an instance of ServiceTypeElement
```
Generated comment:
```
Creates a new element for the given element.
```
---
id444
Code snippet:
```
public Object object(){
  return str();
}
```
Original comment:
```
Since this object is incomplete without the length and the offset, we  have to convert to a string when this function is called.
```
Generated comment:
```
Returns the result of interpreting the object as an instance of \'<em>eobject</em>\'. <!-- begin-user-doc --> this implementation returns null; returning a non-null result will terminate the switch. <!-- end-user-doc -->.
```
---
id445
Code snippet:
```
public void internalEntityDecl(String name,String value) throws SAXException {
}
```
Original comment:
```
Report an internal entity declaration. <p>Only the effective (first) declaration for each entity will be reported.</p>
```
Generated comment:
```
Receive notification of the end of a namespace mapping. <p>by default, do nothing. application writers may override this method in a subclass to take specific actions at the end of each element (such as finalising a tree node or writing output to a file).</p>.
```
---
id446
Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(hc_nodedocumentnodevalue.class,args);
}
```
Original comment:
```
Runs this test from the command line.
```
Generated comment:
```
Runs this test from the command line.
```
---
id447
Code snippet:
```
public static void initializeProperties(String propertyName,String propertyValue){
  SystemPropertiesManager.initializeProperties(propertyName,propertyValue);
}
```
Original comment:
```
Initializes the properties map.
```
Generated comment:
```
Initializes the properties with the given properties.
```
---
id448
Code snippet:
```
public void commitEdit() throws ParseException {
  JFormattedTextField ftf=getTextField();
  ftf.commitEdit();
}
```
Original comment:
```
Pushes the currently edited value to the <code>SpinnerModel</code>. <p> The default implementation invokes <code>commitEdit</code> on the <code>JFormattedTextField</code>.
```
Generated comment:
```
Swfactions interface.
```
---
id449
Code snippet:
```
protected int countEntireIndexRange(int indexOffset){
  seek(indexOffset);
  int count=getCard16();
  if (count == 0)   return 2;
 else {
    int indexOffSize=getCard8();
    seek(indexOffset + 2 + 1+ count * indexOffSize);
    int size=getOffset(indexOffSize) - 1;
    return 2 + 1 + (count + 1) * indexOffSize + size;
  }
}
```
Original comment:
```
Function computes the size of an index
```
Generated comment:
```
Counts the number of entries in the list.
```
---
id450
Code snippet:
```
final int internalNextInt(int origin,int bound){
  int r=mix32(nextSeed());
  if (origin < bound) {
    int n=bound - origin, m=n - 1;
    if ((n & m) == 0)     r=(r & m) + origin;
 else     if (n > 0) {
      for (int u=r >>> 1; u + m - (r=u % n) < 0; u=mix32(nextSeed()) >>> 1)       ;
      r+=origin;
    }
 else {
      while (r < origin || r >= bound)       r=mix32(nextSeed());
    }
  }
  return r;
}
```
Original comment:
```
The form of nextInt used by IntStream Spliterators. Exactly the same as long version, except for types.
```
Generated comment:
```
The form of nextint used by longstream spliterators.
```
---
id451
Code snippet:
```
protected void writeLineSeparator() throws IOException {
  boolean oldReplace=replaceEntities;
  replaceEntities=false;
  super.writeLineSeparator();
  replaceEntities=oldReplace;
  indented=false;
}
```
Original comment:
```
Writes the line separator. This is overriden to make sure we don\'t replace the newline content in case it is outside normal ascii.
```
Generated comment:
```
Write a line.
```
---
id452
Code snippet:
```
public BooleanString(String identifier,AbstractTagFrameBody frameBody){
  super(identifier,frameBody);
}
```
Original comment:
```
Creates a new ObjectBooleanString datatype.
```
Generated comment:
```
Creates a new tag.
```
---
id453
Code snippet:
```
public void paintToolBarContentBackground(SynthContext context,Graphics g,int x,int y,int w,int h){
}
```
Original comment:
```
Paints the background of the tool bar\'s content area.
```
Generated comment:
```
Paints the background of a tabbed pane.
```
---
id454
Code snippet:
```
public void testApp(){
  assertTrue(true);
}
```
Original comment:
```
Rigourous Test :-)
```
Generated comment:
```
Test of getinstance method, of class abstractthrottle.
```
---
id455
Code snippet:
```
public ECPRequestImpl(Element element) throws SAML2Exception {
  parseElement(element);
}
```
Original comment:
```
Constructs the <code>ECPRequest</code> Object.
```
Generated comment:
```
Creates a new element object.
```
---
id456
Code snippet:
```
public FrameBodyDeprecated(AbstractID3v2FrameBody frameBody){
  this.originalFrameBody=frameBody;
}
```
Original comment:
```
Creates a new FrameBodyDeprecated wrapper around the frameBody
```
Generated comment:
```
Creates a new frame.
```
---
id457
Code snippet:
```
public void update(byte[] input){
  engineUpdate(input,0,input.length);
  state=IN_PROGRESS;
}
```
Original comment:
```
Updates the digest using the specified array of bytes.
```
Generated comment:
```
Updates the digest with the byte array.
```
---
id458
Code snippet:
```
@Override public void toString(StringBuilder buffer){
  buffer.append(\"AbandonRequest(idToAbandon=\");
  buffer.append(idToAbandon);
  buffer.append(\")\");
}
```
Original comment:
```
Appends a string representation of this LDAP protocol op to the provided buffer.
```
Generated comment:
```
Appends the specified request to the end of the request.
```
---
id459
Code snippet:
```
public final void testGetName(){
  String name=\"someName\";
  ECGenParameterSpec ps=new ECGenParameterSpec(name);
  assertEquals(name,ps.getName());
}
```
Original comment:
```
Test for <code>getName()</code> method<br> Assertion: returns the <code>name</code>
```
Generated comment:
```
Test for <code>getinstance(string algorithm, string provider)</code> method assertion: throws nullpointerexception when algorithm is null; throws nosuchalgorithmexception when algorithm is not correct;.
```
---
id460
Code snippet:
```
public void rejectedExecution(Runnable r,ThreadPoolExecutor e){
  throw new RejectedExecutionException(\"Task \" + r.toString() + \" rejected from \"+ e.toString());
}
```
Original comment:
```
Always throws RejectedExecutionException.
```
Generated comment:
```
Subscribe to the specified pool.
```
---
id461
Code snippet:
```
protected void uploadWar(PrintWriter writer,HttpServletRequest request,File war,StringManager smClient) throws IOException {
  if (war.exists() && !war.delete()) {
    String msg=smClient.getString(\"managerServlet.deleteFail\",war);
    throw new IOException(msg);
  }
  try (ServletInputStream istream=request.getInputStream();BufferedOutputStream ostream=new BufferedOutputStream(new FileOutputStream(war),1024)){
    byte buffer[]=new byte[1024];
    while (true) {
      int n=istream.read(buffer);
      if (n < 0) {
        break;
      }
      ostream.write(buffer,0,n);
    }
  }
 catch (  IOException e) {
    if (war.exists() && !war.delete()) {
      writer.println(smClient.getString(\"managerServlet.deleteFail\",war));
    }
    throw e;
  }
}
```
Original comment:
```
Upload the WAR file included in this request, and store it at the specified file location.
```
Generated comment:
```
Read the contents of a file.
```
---
id462
Code snippet:
```
public static JsonValue content(final Object object){
  return json(object);
}
```
Original comment:
```
Creates a JSON value for the provided object.
```
Generated comment:
```
Convert an object to json byte array.
```
---
id463
Code snippet:
```
public ExtendedResponseProtocolOp(int resultCode,LocalizableMessage errorMessage,DN matchedDN,List<String> referralURLs){
  this.resultCode=resultCode;
  this.errorMessage=errorMessage;
  this.matchedDN=matchedDN;
  this.referralURLs=referralURLs;
}
```
Original comment:
```
Creates a new extended response protocol op with the provided information.
```
Generated comment:
```
Constructs a new exception with the specified detail message. the cause is not initialized.
```
---
id464
Code snippet:
```
public void persist(@NonNull final String module,@NonNull final String key,@NonNull final String value){
  persist(module,key,null,value);
}
```
Original comment:
```
saves the value into the database.
```
Generated comment:
```
Stores the given value in the configuration.
```
---
id465
Code snippet:
```
public void testZeroNeg(){
  byte aBytes[]={0};
  byte bBytes[]={-2,-3,-4,-4,5,14,23,39,48,57,66,5,14,23};
  int aSign=0;
  int bSign=-1;
  byte rBytes[]={-1,1,2,3,3,-6,-15,-24,-40,-49,-58,-67,-6,-15,-23};
  BigInteger aNumber=new BigInteger(aSign,aBytes);
  BigInteger bNumber=new BigInteger(bSign,bBytes);
  BigInteger result=aNumber.or(bNumber);
  byte resBytes[]=new byte[rBytes.length];
  resBytes=result.toByteArray();
  for (int i=0; i < resBytes.length; i++) {
    assertTrue(resBytes[i] == rBytes[i]);
  }
  assertEquals(\"incorrect sign\",-1,result.signum());
}
```
Original comment:
```
Or for zero and a negative number
```
Generated comment:
```
Flipbit(int n) outside a negative number.
```
---
id466
Code snippet:
```
public OpenDataException(){
  super();
}
```
Original comment:
```
An OpenDataException with no detail message.
```
Generated comment:
```
Constructs a new exception with <code>null</code> as its detail message. the cause is not initialized.
```
---
id467
Code snippet:
```
public boolean unregisterModifiedIndex(AbstractIndexDescriptor index){
  Set<AbstractIndexDescriptor> toRemove=new HashSet<>();
  for (  AbstractIndexDescriptor i : modifiedIndexes) {
    if (i.getName().equalsIgnoreCase(index.getName()) && i.getBackend().getBackendID().equalsIgnoreCase(index.getBackend().getBackendID()) && i.getClass().equals(index.getClass())) {
      toRemove.add(i);
    }
  }
  if (!toRemove.isEmpty()) {
    boolean returnValue=modifiedIndexes.removeAll(toRemove);
    indexModified(toRemove.iterator().next());
    return returnValue;
  }
  return false;
}
```
Original comment:
```
Unregisters a modified index.
```
Generated comment:
```
Unregisters a previously registered index.
```
---
id468
Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  String documentValue;
  doc=(Document)load(\"hc_staff\",false);
  documentValue=doc.getNodeValue();
  assertNull(\"documentNodeValue\",documentValue);
}
```
Original comment:
```
Runs the test case.
```
Generated comment:
```
Runs the test case.
```
---
id469
Code snippet:
```
public void deleteDiscoEntries(Integer[] array){
  for (int i=(array.length - 1); i >= 0; --i) {
    discoData.remove(array[i].intValue());
  }
}
```
Original comment:
```
Deletes the resource offering entries.
```
Generated comment:
```
Removes the specified element from the priority queue.
```
---
id470
Code snippet:
```
public static DN makeChildDN(DN parentDN,AttributeType rdnAttrType,String rdnStringValue){
  ByteString attrValue=ByteString.valueOfUtf8(rdnStringValue);
  return parentDN.child(new RDN(rdnAttrType,attrValue));
}
```
Original comment:
```
Create a new child DN from a given parent DN.  The child RDN is formed from a given attribute type and string value.
```
Generated comment:
```
Creates a new instance.
```
---
id471
Code snippet:
```
public LockableFileWriter(String fileName,boolean append,String lockDir) throws IOException {
  this(new File(fileName),append,lockDir);
}
```
Original comment:
```
Constructs a LockableFileWriter.
```
Generated comment:
```
Creates a new <code>filelock</code> object.
```
---
id472
Code snippet:
```
public void addCallParam(String pattern,int paramIndex){
  addRule(pattern,new CallParamRule(paramIndex));
}
```
Original comment:
```
Add a \"call parameter\" rule for the specified parameters.
```
Generated comment:
```
Adds a new parameter to the end of the list.
```
---
id473
Code snippet:
```
public java.lang.Object newInstance(java.lang.Class javaContentInterface) throws javax.xml.bind.JAXBException {
  return super.newInstance(javaContentInterface);
}
```
Original comment:
```
Create an instance of the specified Java content interface.
```
Generated comment:
```
Creates a new instance.
```
---
id474
Code snippet:
```
protected long outputOffset(){
  return _bytesWritten + _outputTail;
}
```
Original comment:
```
Method for accessing offset of the next byte within the whole output stream that this generator has produced.
```
Generated comment:
```
Returns the number of bytes currently being used to store the values in this cache. this may be greater than the max size if a background deletion is pending.
```
---
id475
Code snippet:
```
public HttpServletRequestWrapper(HttpServletRequest request){
  super(request);
}
```
Original comment:
```
Constructs a request object wrapping the given request.
```
Generated comment:
```
Creates a new request.
```
---
id476
Code snippet:
```
private void failIfDeleted(){
  if (isDeleted()) {
    throw new IllegalStateException(\"Operation failed: element is deleted\");
  }
}
```
Original comment:
```
Fails if this element has been deleted previously by throwing an IllegalStateException.
```
Generated comment:
```
Delete the operation.
```
---
id477
Code snippet:
```
protected PStmtKey createKey(final String sql,final StatementType stmtType){
  String catalog=null;
  try {
    catalog=getCatalog();
  }
 catch (  final SQLException e) {
  }
  return new PStmtKey(normalizeSQL(sql),catalog,stmtType,null);
}
```
Original comment:
```
Create a PStmtKey for the given arguments.
```
Generated comment:
```
Creates a new prepared statement.
```
---
id478
Code snippet:
```
public synchronized void removeObject(NSObject obj){
  set.remove(obj);
}
```
Original comment:
```
Removes an object from the set.
```
Generated comment:
```
Removes the specified object from the set.
```
---
id479
Code snippet:
```
boolean casNext(Node<K,V> cmp,Node<K,V> val){
  return UNSAFE.compareAndSwapObject(this,nextOffset,cmp,val);
}
```
Original comment:
```
compareAndSet next field
```
Generated comment:
```
Returns <tt>true</tt> if this deque contains the specified element. more formally, returns <tt>true</tt> if and only if this deque contains at least one element <tt>e</tt> such that <tt>o.equals(e)</tt>.
```
---
id480
Code snippet:
```
@Override public void run(){
  while (!shutdown) {
    try {
      ReplicationMsg msg=rb.receive();
      rb.updateWindowAfterReplay();
      if (msg != null) {
        debugInfo(\"Broker \" + serverId + \" reader received: \"+ msg);
      }
      lastMsg=msg;
    }
 catch (    SocketTimeoutException ex) {
      if (shutdown) {
        return;
      }
    }
  }
  debugInfo(\"Broker \" + serverId + \" reader thread is dying\");
}
```
Original comment:
```
Loop reading and throwing update messages.
```
Generated comment:
```
Start the server.
```
---
id481
Code snippet:
```
@Override public boolean equals(Object obj){
  if (obj == this) {
    return true;
  }
  if (!(obj instanceof RC5ParameterSpec)) {
    return false;
  }
  RC5ParameterSpec ps=(RC5ParameterSpec)obj;
  return (version == ps.version) && (rounds == ps.rounds) && (wordSize == ps.wordSize)&& (Arrays.equals(iv,ps.iv));
}
```
Original comment:
```
Compares the specified object with this <code>RC5ParameterSpec</code> instance.
```
Generated comment:
```
Compares the two parameters.
```
---
id482
Code snippet:
```
public boolean hasUnsupportedCriticalExtension(){
  Set extns=getCriticalExtensionOIDs();
  return extns != null && !extns.isEmpty();
}
```
Original comment:
```
Will return true if any extensions are present and marked as critical as we currently don\'t handle any extensions!
```
Generated comment:
```
Returns whether it has the extension.
```
---
id483
Code snippet:
```
private void cancelAcquire(Node node){
  if (node == null)   return;
  node.thread=null;
  Node pred=node.prev;
  while (pred.waitStatus > 0)   node.prev=pred=pred.prev;
  Node predNext=pred.next;
  node.waitStatus=Node.CANCELLED;
  if (node == tail && compareAndSetTail(node,pred)) {
    compareAndSetNext(pred,predNext,null);
  }
 else {
    int ws;
    if (pred != head && ((ws=pred.waitStatus) == Node.SIGNAL || (ws <= 0 && compareAndSetWaitStatus(pred,ws,Node.SIGNAL))) && pred.thread != null) {
      Node next=node.next;
      if (next != null && next.waitStatus <= 0)       compareAndSetNext(pred,predNext,next);
    }
 else {
      unparkSuccessor(node);
    }
    node.next=node;
  }
}
```
Original comment:
```
Cancels an ongoing attempt to acquire.
```
Generated comment:
```
Acquires in shared uninterruptible mode.
```
---
id484
Code snippet:
```
protected void handleStart(File startDirectory,Collection<T> results) throws IOException {
}
```
Original comment:
```
Overridable callback method invoked at the start of processing. <p> This implementation does nothing.
```
Generated comment:
```
This method is called when the directory is opened.
```
---
id485
Code snippet:
```
public static XMPDateTime convertToLocalTime(XMPDateTime dateTime){
  long timeInMillis=dateTime.getCalendar().getTimeInMillis();
  GregorianCalendar cal=new GregorianCalendar();
  cal.setTimeInMillis(timeInMillis);
  return new XMPDateTimeImpl(cal);
}
```
Original comment:
```
Make sure a time is local. If the time zone is not the local zone, the time is adjusted and the time zone set to be local.
```
Generated comment:
```
Convert a java.util.date to a java.time.
```
---
id486
Code snippet:
```
public boolean containsCookie(String cookieStr,String cookieName){
  boolean foundCookieName=false;
  String cookieNameInStr=null;
  if (sessionDebug.messageEnabled()) {
    sessionDebug.message(\"CookieNameStr is :\" + cookieNameInStr);
    sessionDebug.message(\"cookieName is :\" + cookieName);
  }
  if (!StringUtils.isBlank(cookieStr)) {
    cookieNameInStr=cookieStr.substring(0,cookieStr.indexOf(\"=\"));
  }
  if ((cookieNameInStr != null) && (cookieNameInStr.equals(cookieName))) {
    foundCookieName=true;
  }
  return foundCookieName;
}
```
Original comment:
```
Checks if the cookie name is in the cookie string.
```
Generated comment:
```
Returns true if the given cookie is valid.
```
---
id487
Code snippet:
```
public static DynamicMBean createMBean(ContextEnvironment environment) throws Exception {
  String mname=createManagedName(environment);
  ManagedBean managed=registry.findManagedBean(mname);
  if (managed == null) {
    Exception e=new Exception(\"ManagedBean is not found with \" + mname);
    throw new MBeanException(e);
  }
  String domain=managed.getDomain();
  if (domain == null)   domain=mserver.getDefaultDomain();
  DynamicMBean mbean=managed.createMBean(environment);
  ObjectName oname=createObjectName(domain,environment);
  if (mserver.isRegistered(oname)) {
    mserver.unregisterMBean(oname);
  }
  mserver.registerMBean(mbean,oname);
  return (mbean);
}
```
Original comment:
```
Create, register, and return an MBean for this <code>ContextEnvironment</code> object.
```
Generated comment:
```
Creates a new <code>gemfire</code> object.
```
---
id488
Code snippet:
```
public final int compare(Object obj1,Object obj2){
  byte[] bytes1=(byte[])obj1;
  byte[] bytes2=(byte[])obj2;
  return (bytes1[0] | 0x20) - (bytes2[0] | 0x20);
}
```
Original comment:
```
Compare two byte arrays, by the order of their tags, as defined in ITU-T X.680, sec. 6.4. (First compare tag classes, then tag numbers, ignoring the constructivity bit.)
```
Generated comment:
```
Compares two byte arrays.
```
---
id489
Code snippet:
```
protected Expression and(int opPos) throws TransformerException {
  return compileOperation(new And(),opPos);
}
```
Original comment:
```
Compile an \'and\' operation.
```
Generated comment:
```
Compile a template.
```
---
id490
Code snippet:
```
public void paint(Graphics a,JComponent b){
  for (int i=0; i < uis.size(); i++) {
    ((ComponentUI)(uis.elementAt(i))).paint(a,b);
  }
}
```
Original comment:
```
Invokes the <code>paint</code> method on each UI handled by this object.
```
Generated comment:
```
Invokes the <code>paint</code> method on each ui handled by this object.
```
---
id491
Code snippet:
```
public FSSAMLServiceViewBean(){
  super(\"FSSAMLService\");
  setDefaultDisplayURL(DEFAULT_DISPLAY_URL);
}
```
Original comment:
```
Creates a personal profile service profile view bean.
```
Generated comment:
```
Creates a new instance of the switch. <!-- begin-user-doc --> <!-- end-user-doc -->.
```
---
id492
Code snippet:
```
public static Reflect on(String name,ClassLoader classLoader) throws ReflectException {
  return on(forName(name,classLoader));
}
```
Original comment:
```
Wrap a class name, loading it via a given class loader. <p> This is the same as calling <code>on(Class.forName(name, classLoader))</code>
```
Generated comment:
```
Creates a new instance of the specified class loader.
```
---
id493
Code snippet:
```
public void addChild(int index,XMPNode node) throws XMPException {
  assertChildNotExisting(node.getName());
  node.setParent(this);
  getChildren().add(index - 1,node);
}
```
Original comment:
```
Adds a node as child to this node.
```
Generated comment:
```
Add a new node to the tree.
```
---
id494
Code snippet:
```
private void registerAuth(LDAPURL ldapUrl,DN dn,String pw,boolean connect) throws LdapException {
  String key=makeKeyFromLDAPUrl(ldapUrl);
  final AuthRecord ar=new AuthRecord();
  ar.dn=dn;
  ar.password=pw;
  if (connect) {
    createLDAPConnection(ldapUrl,ar).close();
  }
synchronized (this) {
    authTable.put(key,ar);
    ConnectionRecord cr=connectionTable.get(key);
    if (cr != null) {
      if (cr.counter <= 0) {
        disconnectAndRemove(cr);
      }
 else {
        cr.disconnectAfterUse=true;
      }
    }
  }
  notifyListeners();
}
```
Original comment:
```
Register authentication data. If authentication data are already available for the protocol/host/port specified in the LDAPURl, they are replaced by the new data. If true is passed as \'connect\' parameter, registerAuth() creates the connection and attempts to connect() and bind() . If connect() or bind() fail, registerAuth() forwards the LdapException and does not register the authentication data.
```
Generated comment:
```
Registers a new client with the given credentials.
```
---
id495
Code snippet:
```
public final void testGetPolicyQualifier01() throws IOException {
  byte[] encoding=getDerEncoding();
  byte[] pqEncoding=new byte[28];
  System.arraycopy(encoding,12,pqEncoding,0,pqEncoding.length);
  PolicyQualifierInfo i=new PolicyQualifierInfo(encoding);
  byte[] pqEncodingRet=i.getPolicyQualifier();
  assertTrue(Arrays.equals(pqEncoding,pqEncodingRet));
}
```
Original comment:
```
Test #1 for <code>getPolicyQualifier()</code> method Assertion: Returns the ASN.1 DER encoded form of this <code>PolicyQualifierInfo</code>
```
Generated comment:
```
Test for <code>getinstance(string algorithm, string provider)</code> method assertion: throws nullpointerexception when algorithm is null; throws nosuchalgorithmexception when algorithm is not correct;.
```
---
id496
Code snippet:
```
public boolean deleteAll(){
  return database.delete(DATABASE_TABLE,null,null) > 0;
}
```
Original comment:
```
Delete all RuleAction records.
```
Generated comment:
```
This method was generated by mybatis generator. this method corresponds to the database table user_todo.
```
---
id497
Code snippet:
```
public CertificateNotYetValidException(){
  super();
}
```
Original comment:
```
Constructs a CertificateNotYetValidException with no detail message. A detail message is a String that describes this particular exception.
```
Generated comment:
```
Constructs a certificateexception with no detail message. a detail message is a string that describes this particular exception.
```
---
id498
Code snippet:
```
private Object writeReplace(){
  return new Ser(Ser.ZONE_REGION_TYPE,this);
}
```
Original comment:
```
Writes the object using a <a href=\"../../serialized-form.html#java.time.Ser\">dedicated serialized form</a>.
```
Generated comment:
```
Writes the object to the output stream.
```
---
id499
Code snippet:
```
public PdfSignatureBuildProperties(PdfDictionary dict){
  super(dict);
}
```
Original comment:
```
Creates new PdfSignatureBuildProperties with preset values.
```
Generated comment:
```
Creates a new instance.
```
---
