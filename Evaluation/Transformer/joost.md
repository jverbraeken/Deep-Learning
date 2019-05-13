id: 400

Code snippet:
```
public com.sun.identity.wsfederation.jaxb.wsspolicy.AbsXPathElement createAbsXPathElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.wsfederation.jaxb.wsspolicy.impl.AbsXPathElementImpl();
}
```
Comment:
```
<!-- begin-user-doc --> <!-- end-user-doc -->
```
---
id: 401

Code snippet:
```
@Override public void clearWhiteList(){
  SharedPreferences.Editor editor=sharedPreferences.edit();
  editor.remove(KEY_WHITELIST);
  editor.commit();
}
```
Comment:
```
Clears the list.
```
---
id: 402

Code snippet:
```
public void removeNotify(){
  super.removeNotify();
  firePropertyChange(\"ancestor\",getParent(),null);
  unregisterWithKeyboardManager();
  deregisterNextFocusableComponent();
  if (getCreatedDoubleBuffer()) {
    RepaintManager.currentManager(this).resetDoubleBuffer();
    setCreatedDoubleBuffer(false);
  }
  if (autoscrolls) {
    Autoscroller.stop(this);
  }
}
```
Comment:
```
Notifies this component that it no longer has a parent component. When this method is invoked, any <code>KeyboardAction</code>s set up in the the chain of parent components are removed. This method is called by the toolkit internally and should not be called directly by programs.
```
---
id: 403

Code snippet:
```
public static SearchRequest newSearchRequest(final DN name,final SearchScope scope,final Filter filter,final String... attributeDescriptions){
  return Requests.newSearchRequest(name,scope,filter,attributeDescriptions).addControl(TransactionIdControl.newControl(AuditRequestContext.createSubTransactionIdValue()));
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 404

Code snippet:
```
public SAML2MetaException(String message){
  super(message);
}
```
Comment:
```
Constructs a new <code>SAML2MetaException</code> with the given message.
```
---
id: 405

Code snippet:
```
public static int broadcast(String message,String permission){
  return server.broadcast(message,permission);
}
```
Comment:
```
Broadcasts the specified message to every user with the given permission name.
```
---
id: 406

Code snippet:
```
public void writeExif(String jpegFileName,String exifOutFileName) throws FileNotFoundException, IOException {
  if (jpegFileName == null || exifOutFileName == null) {
    throw new IllegalArgumentException(NULL_ARGUMENT_STRING);
  }
  InputStream is=null;
  try {
    is=new FileInputStream(jpegFileName);
    writeExif(is,exifOutFileName);
  }
 catch (  IOException e) {
    closeSilently(is);
    throw e;
  }
  is.close();
}
```
Comment:
```
Writes the tags from this ExifInterface object into a jpeg file, removing prior exif tags.
```
---
id: 407

Code snippet:
```
public com.sun.identity.liberty.ws.common.jaxb.ac.GoverningAgreementsElement createGoverningAgreementsElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.liberty.ws.common.jaxb.ac.impl.GoverningAgreementsElementImpl();
}
```
Comment:
```
Create an instance of GoverningAgreementsElement
```
---
id: 408

Code snippet:
```
public A last(){
  A last=null;
  ImmutableList<A> t=this;
  while (t.tail != null) {
    last=t.head;
    t=t.tail;
  }
  return last;
}
```
Comment:
```
Returns an array containing all of the elements in this queue, in proper sequence. <p>The returned array will be \"safe\" in that no references to it are maintained by this queue.  (In other words, this method must allocate a new array).  The caller is thus free to modify the returned array. <p>This method acts as bridge between array-based and collection-based APIs.
```
---
id: 409

Code snippet:
```
public ByteBufferOutputStream append(String str){
  if (str != null)   return append(str.getBytes(StandardCharsets.ISO_8859_1));
  return this;
}
```
Comment:
```
Appends a <CODE>String</CODE> to the buffer. The <CODE>String</CODE> is converted according to the encoding ISO-8859-1.
```
---
id: 410

Code snippet:
```
public void registerClassHandler(ClassHandler handler){
  classHandlers.add(handler);
}
```
Comment:
```
Registers the given class.
```
---
id: 411

Code snippet:
```
@Override public synchronized void write(int b){
  int inBufferPos=count - filledBufferSum;
  if (inBufferPos == currentBuffer.length) {
    needNewBuffer(count + 1);
    inBufferPos=0;
  }
  currentBuffer[inBufferPos]=(byte)b;
  count++;
}
```
Comment:
```
Writes the buffer to the underlying stream.
```
---
id: 412

Code snippet:
```
public boolean isCancelled(){
  return useInteractedBlock() == Result.DENY;
}
```
Comment:
```
Gets the cancellation state of this event. Set to true if you want to prevent buckets from placing water and so forth
```
---
id: 413

Code snippet:
```
public static void removeServerConfiguration(SSOToken ssoToken,String instanceName,Collection propertyNames) throws SMSException, SSOException, IOException {
  ServiceConfig cfg=getServerConfig(ssoToken,instanceName);
  if (cfg != null) {
    Map map=cfg.getAttributes();
    Set set=(Set)map.get(ATTR_SERVER_CONFIG);
    Properties properties=getProperties(set);
    for (Iterator i=properties.keySet().iterator(); i.hasNext(); ) {
      String key=(String)i.next();
      if (propertyNames.contains(key)) {
        i.remove();
      }
    }
    map.put(ATTR_SERVER_CONFIG,getPropertiesSet(properties));
    cfg.setAttributes(map);
  }
}
```
Comment:
```
Removes the properties from the given properties.
```
---
id: 414

Code snippet:
```
public static ListSubCommandHandler create(SubCommandArgumentParser parser,ManagedObjectPath<?,?> p,SetRelationDefinition<?,?> r) throws ArgumentException {
  return new ListSubCommandHandler(parser,p,r,r.getPluralName(),r.getUserFriendlyPluralName());
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 415

Code snippet:
```
public FrameBodyTPRO(byte textEncoding,String text){
  super(textEncoding,text);
}
```
Comment:
```
Creates a new instance.
```
---
id: 416

Code snippet:
```
public void deleteField(String id){
  super.doDeleteTagField(new FrameAndSubId(id,null));
}
```
Comment:
```
Delete fields with this (frame) id
```
---
id: 417

Code snippet:
```
public void paintDesktopPaneBackground(SynthContext context,Graphics g,int x,int y,int w,int h){
  paintBackground(context,g,x,y,w,h,null);
}
```
Comment:
```
Paints the background of a desktop pane.
```
---
id: 418

Code snippet:
```
public boolean equals(Object obj){
  if (obj == this)   return true;
  if (!(obj instanceof MBeanPermission))   return false;
  MBeanPermission that=(MBeanPermission)obj;
  return (this.mask == that.mask) && (this.getName().equals(that.getName()));
}
```
Comment:
```
Checks two MBeanPermission objects for equality. Checks that <i>obj</i> is an MBeanPermission, and has the same name and actions as this object. <P>
```
---
id: 419

Code snippet:
```
public ConsonantVowelNameGenerator build() throws IllegalStateException {
  checkState();
  return new ConsonantVowelNameGenerator(this);
}
```
Comment:
```
Uses the builder to construct a new ConsonantVowelNameGenerator.
```
---
id: 420

Code snippet:
```
public boolean isEnabled(){
  return logStatus;
}
```
Comment:
```
Ruft den Wert der enabled-Eigenschaft ab.
```
---
id: 421

Code snippet:
```
@DataProvider(name=\"mixedMatches\") public Object[][] mixedData(){
  return new Object[][]{{\"12AB:0000:0000:CD30:0000:0000:0000:0000\"},{\"12ab:0:0:cd3f:0000:0000:23DC:DC30\"},{\"45.56.33.9\"},{\"72.56.78.9\"},{\"56.56.78.9\"}};
}
```
Comment:
```
Returns an array containing all of the elements in this queue, in proper sequence. <p>The returned array will be \"safe\" in that no references to it are maintained by this queue.  (In other words, this method must allocate a new array).  The caller is thus free to modify the returned array. <p>This method acts as bridge between array-based and collection-based APIs.
```
---
id: 422

Code snippet:
```
public String toXMLString(boolean includeNSPrefix,boolean declareNS) throws XACMLException {
  StringBuffer sb=new StringBuffer(2000);
  String nsPrefix=\"\";
  String nsDeclaration=\"\";
  if (includeNSPrefix) {
    nsPrefix=XACMLConstants.CONTEXT_NS_PREFIX + \":\";
  }
  if (declareNS) {
    nsDeclaration=XACMLConstants.CONTEXT_NS_DECLARATION;
  }
  sb.append(\"<\").append(nsPrefix).append(XACMLConstants.RESPONSE).append(nsDeclaration).append(\">
\");
  int length=0;
  if (results != null) {
    length=results.size();
    for (int i=0; i < length; i++) {
      Result result=(Result)results.get(i);
      sb.append(result.toXMLString(includeNSPrefix,false));
    }
  }
  sb.append(\"</\").append(nsPrefix).append(XACMLConstants.RESPONSE).append(\">
\");
  return sb.toString();
}
```
Comment:
```
Returns a string representation of this object.
```
---
id: 423

Code snippet:
```
public static void warning(String msg){
  debugInst.debug(IDebug.WARNING,msg);
}
```
Comment:
```
warning level debug message
```
---
id: 424

Code snippet:
```
TemplateFile(Schema schema,Map<String,String> constants,String resourcePath) throws IOException {
  this(schema,constants,resourcePath,new Random(),true);
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 425

Code snippet:
```
SOAPMessage toSOAPMessage() throws SOAPBindingException {
  return Utils.DocumentToSOAPMessage(toDocument(true));
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 426

Code snippet:
```
public ObjectInUseException(String msg,String name,Object user){
  super(msg);
  this.name=name;
  this.user=user;
}
```
Comment:
```
Constructs an <code>ObjectInUseException</code> object
```
---
id: 427

Code snippet:
```
public Reflect call(String name) throws ReflectException {
  return call(name,new Object[0]);
}
```
Comment:
```
Call a method by its name. <p> This is a convenience method for calling <code>call(name, new Object[0])</code>
```
---
id: 428

Code snippet:
```
static int readUnsignedShort(final byte[] b,final int index){
  return ((b[index] & 0xFF) << 8) | (b[index + 1] & 0xFF);
}
```
Comment:
```
Reads a signed short value in the given byte array.
```
---
id: 429

Code snippet:
```
public boolean tryUnlockRead(){
  long s, m;
  WNode h;
  while ((m=(s=state) & ABITS) != 0L && m < WBIT) {
    if (m < RFULL) {
      if (U.compareAndSwapLong(this,STATE,s,s - RUNIT)) {
        if (m == RUNIT && (h=whead) != null && h.status != 0)         release(h);
        return true;
      }
    }
 else     if (tryDecReaderOverflow(s) != 0L)     return true;
  }
  return false;
}
```
Comment:
```
Unlock head field.
```
---
id: 430

Code snippet:
```
public char first(){
  pos=begin;
  return current();
}
```
Comment:
```
Returns the character at the current position.
```
---
id: 431

Code snippet:
```
void clear(){
  baseDNs.clear();
  privateNamingContexts.clear();
  publicNamingContexts.clear();
  allPublicNamingContexts.clear();
}
```
Comment:
```
Clear and nullify this registry\'s internal state.
```
---
id: 432

Code snippet:
```
protected NameValue qheader() throws ParseException {
  String name=lexer.getNextToken(\'=\');
  lexer.consume(1);
  String value=hvalue();
  return new NameValue(name,value,false);
}
```
Comment:
```
Get a name value for a given query header (ie one that comes after the ?).
```
---
id: 433

Code snippet:
```
public String encode(){
  String encoded_string;
  encoded_string=PHONE_FIELD;
  if (name != null) {
    encoded_string+=name + Separators.LESS_THAN;
  }
  encoded_string+=phoneNumber;
  if (name != null) {
    encoded_string+=Separators.GREATER_THAN;
  }
  encoded_string+=Separators.NEWLINE;
  return encoded_string;
}
```
Comment:
```
Encode into canonical form.
```
---
id: 434

Code snippet:
```
@Override public int hashCode(){
  if (hashCode == 0) {
    if (bytes != null && bytes.length != 0) {
      int len=bytes.length;
      int inc=((len - 32) / 32) + 1;
      for (int i=0; i < len; ) {
        hashCode=(hashCode * 37) + bytes[i];
        i+=inc;
      }
    }
    if (hashCode == 0) {
      hashCode=1;
    }
  }
  return hashCode;
}
```
Comment:
```
Creates a hash code for this CollationKey. Compute the hash by iterating sparsely over about 32 (up to 63) bytes spaced evenly through the string.  For each byte, multiply the previous hash value by a prime number and add the new byte in, like a linear congruential random number generator, producing a pseudo-random deterministic value well distributed over the output range.
```
---
id: 435

Code snippet:
```
private Promise<ActionResponse,ResourceException> internalHandleAction(String tokenId,Context context,ActionRequest request){
  final String action=request.getAction();
  final ActionHandler actionHandler=actionHandlers.get(action);
  if (actionHandler != null) {
    return actionHandler.handle(tokenId,context,request);
  }
 else {
    String message=String.format(\"Action %s not implemented for this resource\",action);
    NotSupportedException e=new NotSupportedException(message);
    if (LOGGER.messageEnabled()) {
      LOGGER.message(\"SessionResource.actionInstance :: \" + message,e);
    }
    return e.asPromise();
  }
}
```
Comment:
```
Handle the action specified by the user (i.e. one of those in the validActions set).
```
---
id: 436

Code snippet:
```
public void removeAccessibleSelection(int i){
  TreeModel model=JTree.this.getModel();
  if (model != null) {
    if (i >= 0 && i < getAccessibleChildrenCount()) {
      TreePath path=getChildTreePath(i);
      JTree.this.removeSelectionPath(path);
    }
  }
}
```
Comment:
```
Removes the specified selected item in the object from the object\'s selection.  If the specified item isn\'t currently selected, this method has no effect.
```
---
id: 437

Code snippet:
```
public MalformedChallengeException(){
  super();
}
```
Comment:
```
Constructs a new exception with <code>null</code> as its detail message. The cause is not initialized.
```
---
id: 438

Code snippet:
```
@Override public void reset() throws IOException {
synchronized (lock) {
    if (isOpen()) {
      pos=markpos != -1 ? markpos : 0;
    }
 else {
      throw new IOException(\"StringReader is closed\");
    }
  }
}
```
Comment:
```
Resets the scanner to read from a new input stream. Does not close the old reader. All internal variables are reset, the old input stream <b>cannot</b> be reused (internal buffer is discarded and lost). Lexical state is set to <tt>YY_INITIAL</tt>.
```
---
id: 439

Code snippet:
```
@Override public void removeAttribute(String name){
  if (!removeSpecial(name))   getRequest().removeAttribute(name);
}
```
Comment:
```
Removes an attribute from the list.
```
---
id: 440

Code snippet:
```
public void testInsertPrepared() throws SQLException {
  PreparedStatement stat=conn.prepareStatement(\"INSERT INTO \" + DatabaseCreator.TEST_TABLE5 + \" VALUES(?, ?)\");
  stat.setInt(1,1);
  stat.setString(2,\"1\");
  stat.execute();
  stat.setInt(1,2);
  stat.setString(2,\"3\");
  stat.execute();
  ResultSet r=statement.executeQuery(\"SELECT COUNT(*) FROM \" + DatabaseCreator.TEST_TABLE5 + \" WHERE (testId = 1 AND testValue = \'1\') \"+ \"OR (testId = 2 AND testValue = \'3\')\");
  r.next();
  assertEquals(\"Incorrect number of records\",2,r.getInt(1));
  r.close();
  stat.close();
}
```
Comment:
```
InsertFunctionalityTest#testInsertFunctionalityTest(). Updates table using PreparedStatement
```
---
id: 441

Code snippet:
```
private void updateDefaultButton(StatusGenericPanel panel){
  ButtonType buttonType=panel.getButtonType();
  if (buttonType == ButtonType.OK_CANCEL) {
    getRootPane().setDefaultButton(okButton);
  }
 else   if (buttonType == ButtonType.OK) {
    getRootPane().setDefaultButton(okButton);
  }
 else   if (buttonType == ButtonType.CLOSE) {
    getRootPane().setDefaultButton(closeButton);
  }
}
```
Comment:
```
Updates the default button of the frame, depending on the type of generic panel that it contains.
```
---
id: 442

Code snippet:
```
public String transformOpenIdConnectToSAML2(SAML2SubjectConfirmation subjectConfirmation,String oidcTokenValue,X509Certificate hokProofCert) throws IOException {
  if (oidcTokenValue == null) {
    throw new IOException(\"OIDC token is null!\");
  }
  OpenIdConnectTokenState tokenState=OpenIdConnectTokenState.builder().tokenValue(oidcTokenValue).build();
  RestSTSTokenTranslationInvocationState invocationState=RestSTSTokenTranslationInvocationState.builder().inputTokenState(tokenState.toJson()).outputTokenState(buildSAML2TokenCreationState(subjectConfirmation,hokProofCert).toJson()).build();
  return invokeTokenTranslation(invocationState.toJson().toString());
}
```
Comment:
```
Invokes a OIDCToken->SAML2 token transformation Sample json posted at the rest-sts instance in this method (HoK SubjectConfirmation, with token elements truncated): { \"input_token_state\": { \"token_type\": \"OPENIDCONNECT\", \"oidc_id_token\": \"eyAiYWxQ.euTNnNDExNTkyMjEyIH0.kuNlKwyvZJqaC8EYpDyPJMiEcII\" },\"output_token_state\": { \"token_type\": \"SAML2\", \"subject_confirmation\": \"HOLDER_OF_KEY\", \"proof_token_state\": { \"base64EncodedCertificate\": \"MIMbFAAOBjQAwgYkCgYEArSQ...c/U75GB2AtKhbGS5pimrW0Y0Q==\" } } } { \"input_token_state\": { \"token_type\": \"OPENIDCONNECT\", \"oidc_id_token\": \"eyAidHlwIjogIkpXVCIsICJhbGciOiAiSFMyNTYiIH0.eyAidG9rZW5OYW1lIjogImlkX3...gMTQ0ODA1MzY52xpZW50IiBdIH0.yKVp4kInTR-6TZGL3cjvA-adhbIfLqjf8E7ZQWHCm9c\" }, \"output_token_state\": { \"token_type\": \"SAML2\", \"subject_confirmation\": \"BEARER\" } } { \"input_token_state\": { \"token_type\": \"OPENIDCONNECT\", \"oidc_id_token\": \"eyAidHlwIjogIkpXVCIsICJhbGciOiAiSFMyNTYiIH0.eyAidG9rZW5O...Q2xpZW50IiBdIH0.yKVp4kInTR-6TZGL3cjvA-adhbIfLqjf8E7ZQWHCm9c\" }, \"output_token_state\": { \"token_type\": \"SAML2\", \"subject_confirmation\": \"SENDER_VOUCHES\" } } To set up oauth2, you have to: 1. configure the OAuth2 provider using the common tasks 2. then create a client using the agents tab - reflecting the client id and the redirect uri defined in my integration test. Also add the openid scope 2.5. Make sure you specify a hmac-based based signing in the OAuth2 client. 3. then create the oidc module - the issuer should be the url of the openam deployment, with oauth2 appended (e.g. http://macbook.dirk.internal.forgerock.com:8080/openam/oauth2), the type should be client-secret, and the secret itself should be that configured for the oauth2 client - we are authN-ing a HMAC-signed jwt. 4. if the OpenAM provider is issuing the oidc token, then the azp and aud in the oidc module should be set to the name of the oauth2 client
```
---
id: 443

Code snippet:
```
public static String toString(InputStream input) throws IOException {
  return toString(input,Charset.defaultCharset());
}
```
Comment:
```
Get the contents of an <code>InputStream</code> as a String using the default character encoding of the platform. <p> This method buffers the input internally, so there is no need to use a <code>BufferedInputStream</code>.
```
---
id: 444

Code snippet:
```
public void startDrag(DragGestureEvent trigger,Cursor dragCursor,Image dragImage,Point imageOffset,Transferable transferable,DragSourceListener dsl,FlavorMap flavorMap) throws InvalidDnDOperationException {
  SunDragSourceContextPeer.setDragDropInProgress(true);
  try {
    if (flavorMap != null)     this.flavorMap=flavorMap;
    DragSourceContextPeer dscp=Toolkit.getDefaultToolkit().createDragSourceContextPeer(trigger);
    DragSourceContext dsc=createDragSourceContext(dscp,trigger,dragCursor,dragImage,imageOffset,transferable,dsl);
    if (dsc == null) {
      throw new InvalidDnDOperationException();
    }
    dscp.startDrag(dsc,dsc.getCursor(),dragImage,imageOffset);
  }
 catch (  RuntimeException e) {
    SunDragSourceContextPeer.setDragDropInProgress(false);
    throw e;
  }
}
```
Comment:
```
Start a drag, given the <code>DragGestureEvent</code> that initiated the drag, the initial <code>Cursor</code> to use, the <code>Image</code> to drag, the offset of the <code>Image</code> origin from the hotspot of the <code>Cursor</code> at the instant of the trigger, the <code>Transferable</code> subject data of the drag, the <code>DragSourceListener</code>, and the <code>FlavorMap</code>. <P>
```
---
id: 445

Code snippet:
```
public StringWriter(int initialSize){
  if (initialSize < 0) {
    throw new IllegalArgumentException(\"Negative buffer size\");
  }
  buf=new StringBuffer(initialSize);
  lock=buf;
}
```
Comment:
```
Creates a new <code>TLongLongHashMap</code> instance with a prime capacity equal to or greater than <tt>initialCapacity</tt> and with the default load factor.
```
---
id: 446

Code snippet:
```
public String toStringImpl(){
  return ip.toString();
}
```
Comment:
```
Used by super class to log the attribute\'s contents when packet logging is enabled.
```
---
id: 447

Code snippet:
```
public static Function<JsonValue,JsonValue,JsonValueException> resolvedLocation(){
  return new ResolveLocationJsonValueFunction();
}
```
Comment:
```
Returns a new instance of the default value.
```
---
id: 448

Code snippet:
```
public boolean verify() throws NoSuchAlgorithmException, NoSuchProviderException, InvalidKeyException, SignatureException {
  return verify(BouncyCastleProvider.PROVIDER_NAME);
}
```
Comment:
```
Verifies that the signature from the server matches the computed signature on the data.  Returns true if the data is correctly signed.
```
---
id: 449

Code snippet:
```
private boolean duplicateTransformsSpecified(Set<String> supportedTokenTransforms){
  Set<String> inputOutputComboSet=new HashSet<>(supportedTokenTransforms.size());
  for (  String transform : supportedTokenTransforms) {
    String[] breakdown=transform.split(REGEX_PIPE);
    String entry=breakdown[0] + breakdown[1];
    if (inputOutputComboSet.contains(entry)) {
      return true;
    }
 else {
      inputOutputComboSet.add(entry);
    }
  }
  return false;
}
```
Comment:
```
The set of possible token transformation definition selections, as defined in the supported-token-transforms property in propertyRestSecurityTokenService.xml, is as follow: USERNAME|SAML2|true USERNAME|SAML2|false OPENIDCONNECT|SAML2|true OPENIDCONNECT|SAML2|false OPENAM|SAML2|true OPENAM|SAML2|false X509|SAML2|true X509|SAML2|false USERNAME|OPENIDCONNECT|true USERNAME|OPENIDCONNECT|false OPENIDCONNECT|OPENIDCONNECT|true OPENIDCONNECT|OPENIDCONNECT|false OPENAM|OPENIDCONNECT|true OPENAM|OPENIDCONNECT|false X509|OPENIDCONNECT|true X509|OPENIDCONNECT|false This method will return true if the supportedTokenTransforms method specified by the user contains more than a single entry for a given input token type per given output token type.
```
---
id: 450

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList genderList;
  Node gender;
  EntityReference entRef;
  Element entElement;
  Attr newAttr;
  Attr badAttr;
  Node appendedChild;
  doc=(Document)load(\"staff\",true);
  genderList=doc.getElementsByTagName(\"gender\");
  gender=genderList.item(2);
  entRef=doc.createEntityReference(\"ent4\");
  assertNotNull(\"createdEntRefNotNull\",entRef);
  appendedChild=gender.appendChild(entRef);
  entElement=(Element)entRef.getFirstChild();
  assertNotNull(\"entElementNotNull\",entElement);
  newAttr=doc.createAttribute(\"newAttr\");
{
    boolean success=false;
    try {
      badAttr=entElement.setAttributeNode(newAttr);
    }
 catch (    DOMException ex) {
      success=(ex.code == DOMException.NO_MODIFICATION_ALLOWED_ERR);
    }
    assertTrue(\"throw_NO_MODIFICATION_ALLOWED_ERR\",success);
  }
}
```
Comment:
```
Runs the test case.
```
---
id: 451

Code snippet:
```
protected EditorKit createDefaultEditorKit(){
  return new PlainEditorKit();
}
```
Comment:
```
Creates the default editor kit (<code>PlainEditorKit</code>) for when the component is first created.
```
---
id: 452

Code snippet:
```
public byte[] remainingBytesZeroTerminated(){
  final int length=byteArray.length - (bytes.position() + 1);
  final byte[] result=nextByteArray(length);
  bytes.skip(1);
  return result;
}
```
Comment:
```
Returns the number of bytes currently being used to store the values in this cache. This may be greater than the max size if a background deletion is pending.
```
---
id: 453

Code snippet:
```
public java.lang.String toString(boolean includeNS,boolean declareNS){
  StringBuffer xml=new StringBuffer(300);
  String o=SAMLUtilsCommon.makeStartElementTagXML(\"DoNotCacheCondition\",includeNS,declareNS);
  xml.append(o);
  o=SAMLUtilsCommon.makeEndElementTagXML(\"DoNotCacheCondition\",includeNS);
  xml.append(o);
  return xml.toString();
}
```
Comment:
```
Returns a String representation of the <code>&lt;DoNotCacheCondition&gt;</code> element.
```
---
id: 454

Code snippet:
```
public DateTimeFormatter withLocale(Locale locale){
  if (this.locale.equals(locale)) {
    return this;
  }
  return new DateTimeFormatter(printerParser,locale,decimalStyle,resolverStyle,resolverFields,chrono,zone);
}
```
Comment:
```
Returns a copy of this date with the specified number of days added. <p> This instance is immutable and unaffected by this method call.
```
---
id: 455

Code snippet:
```
public EventListenerProxy(T listener){
  this.listener=listener;
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 456

Code snippet:
```
public void createRelationType(String relationTypeName,RoleInfo[] roleInfoArray) throws IllegalArgumentException, InvalidRelationTypeException {
  if (relationTypeName == null || roleInfoArray == null) {
    String excMsg=\"Invalid parameter.\";
    throw new IllegalArgumentException(excMsg);
  }
  RELATION_LOGGER.entering(RelationService.class.getName(),\"createRelationType\",relationTypeName);
  RelationType relType=new RelationTypeSupport(relationTypeName,roleInfoArray);
  addRelationTypeInt(relType);
  RELATION_LOGGER.exiting(RelationService.class.getName(),\"createRelationType\");
  return;
}
```
Comment:
```
Creates and persists a new role entity.
```
---
id: 457

Code snippet:
```
private int compareBackendIDs(BaseDNDescriptor desc1,BaseDNDescriptor desc2){
  return desc1.getBackend().getBackendID().compareTo(desc2.getBackend().getBackendID());
}
```
Comment:
```
Compares this entry with another cp_info object (which may reside in a different constant pool).
```
---
id: 458

Code snippet:
```
public void addRestrictedDomain(String domainName){
  if (StringUtils.isEmpty(domainName)) {
    return;
  }
  if (restrictedDomains == null) {
    restrictedDomains=new ArrayList<>();
  }
  restrictedDomains.add(domainName);
}
```
Comment:
```
Adds a new <code>Connection</code> object.
```
---
id: 459

Code snippet:
```
public void externalEntityDecl(String name,String publicId,String systemId) throws SAXException {
}
```
Comment:
```
This method does nothing.
```
---
id: 460

Code snippet:
```
InitializeTargetMsg(byte[] in,short version) throws DataFormatException {
  final ByteArrayScanner scanner=new ByteArrayScanner(in);
  final byte msgType=scanner.nextByte();
  if (msgType != MSG_TYPE_INITIALIZE_TARGET) {
    throw new DataFormatException(\"input is not a valid InitializeDestinationMessage\");
  }
  destination=scanner.nextIntUTF8();
  baseDN=scanner.nextDN();
  senderID=scanner.nextIntUTF8();
  requestorID=scanner.nextIntUTF8();
  entryCount=scanner.nextLongUTF8();
  if (version >= ProtocolVersion.REPLICATION_PROTOCOL_V4) {
    initWindow=scanner.nextIntUTF8();
  }
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 461

Code snippet:
```
public WSFederationMetaException(String errorCode,Object[] args){
  super(WSFederationConstants.BUNDLE_NAME,errorCode,args);
}
```
Comment:
```
Constructs a new <code>WSFederationMetaException</code> without a nested <code>Throwable</code> using default resource bundle.
```
---
id: 462

Code snippet:
```
private static boolean determineNegation(StringBuilder ruleExpr){
  boolean negate=false;
  String ruleStr=ruleExpr.toString();
  while (ruleStr.regionMatches(true,0,\"not \",0,4)) {
    negate=!negate;
    ruleStr=ruleStr.substring(4);
  }
  ruleExpr.replace(0,ruleExpr.length(),ruleStr);
  return negate;
}
```
Comment:
```
Tries to strip an \"not\" boolean modifier from the string and determine at the same time if the value should be flipped. For example: not not not bindrule is true.
```
---
id: 463

Code snippet:
```
public DropTargetDropEvent(DropTargetContext dtc,Point cursorLocn,int dropAction,int srcActions,boolean isLocal){
  this(dtc,cursorLocn,dropAction,srcActions);
  isLocalTx=isLocal;
}
```
Comment:
```
Construct a <code>DropTargetEvent</code> given the <code>DropTargetContext</code> for this operation, the location of the drag <code>Cursor</code>\'s hotspot in the <code>Component</code>\'s coordinates, the currently selected user drop action, the current set of actions supported by the source, and a <code>boolean</code> indicating if the source is in the same JVM as the target. <P>
```
---
id: 464

Code snippet:
```
public final int length(){
  return array.length;
}
```
Comment:
```
Returns the length of the array.
```
---
id: 465

Code snippet:
```
public static boolean isEqual(JsonValue oldValue,JsonValue newValue){
  JsonValue tmpOldValue=null == oldValue ? json(object()) : oldValue.copy();
  JsonValue tmpNewValue=null == newValue ? json(object()) : newValue.copy();
  tmpOldValue.remove(FIELD_CONTENT_ID);
  tmpOldValue.remove(FIELD_CONTENT_REVISION);
  tmpNewValue.remove(FIELD_CONTENT_ID);
  tmpNewValue.remove(FIELD_CONTENT_REVISION);
  return tmpOldValue.isEqualTo(tmpNewValue);
}
```
Comment:
```
Returns true if the given value is a valid object.
```
---
id: 466

Code snippet:
```
protected View createChild(String name){
  View child=null;
  if (name.equals(TITLE_HTML_PAGE)) {
    child=new StaticTextField(this,TITLE_HTML_PAGE,\"\");
  }
 else   if (name.equals(COPYRIGHT_TEXT)) {
    child=new StaticTextField(this,COPYRIGHT_TEXT,\"\");
  }
 else   if (name.equals(ERROR_TITLE)) {
    child=new StaticTextField(this,ERROR_TITLE,\"\");
  }
 else   if (name.equals(ERROR_MSG)) {
    child=new StaticTextField(this,ERROR_MSG,\"\");
  }
 else   if (name.equals(INFO_MSG)) {
    child=new StaticTextField(this,INFO_MSG,\"\");
  }
 else   if (name.equals(LBL_SUN_LOGO)) {
    child=new StaticTextField(this,LBL_SUN_LOGO,\"\");
  }
 else   if (name.equals(LBL_PRODUCT)) {
    child=new StaticTextField(this,LBL_PRODUCT,\"\");
  }
 else   if (name.equals(LBL_JAVA_LOGO)) {
    child=new StaticTextField(this,LBL_JAVA_LOGO,\"\");
  }
 else {
    throw new IllegalArgumentException(\"invalid child name \" + name);
  }
  return child;
}
```
Comment:
```
Creates child component
```
---
id: 467

Code snippet:
```
public static ObjectifyFactory factory(){
  return ObjectifyService.factory();
}
```
Comment:
```
Returns a new instance of this class.
```
---
id: 468

Code snippet:
```
private void reportInterruptAfterWait(int interruptMode) throws InterruptedException {
  if (interruptMode == THROW_IE)   throw new InterruptedException();
 else   if (interruptMode == REINTERRUPT)   selfInterrupt();
}
```
Comment:
```
Throws InterruptedException, reinterrupts current thread, or does nothing, depending on mode.
```
---
id: 469

Code snippet:
```
public com.sun.identity.liberty.ws.idpp.jaxb.LanguageElement createLanguageElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.liberty.ws.idpp.jaxb.impl.LanguageElementImpl();
}
```
Comment:
```
Create an instance of LanguageElement
```
---
id: 470

Code snippet:
```
ObjectStreamField(Field field,boolean unshared,boolean showType){
  this.field=field;
  this.unshared=unshared;
  name=field.getName();
  Class<?> ftype=field.getType();
  type=(showType || ftype.isPrimitive()) ? ftype : Object.class;
  signature=getClassSignature(ftype).intern();
}
```
Comment:
```
Creates a new instance.
```
---
id: 471

Code snippet:
```
private ListResourceBundle loadResourceBundle(String resourceBundle) throws MissingResourceException {
  m_resourceBundleName=resourceBundle;
  Locale locale=getLocale();
  ListResourceBundle lrb;
  try {
    ResourceBundle rb=ResourceBundle.getBundle(m_resourceBundleName,locale);
    lrb=(ListResourceBundle)rb;
  }
 catch (  MissingResourceException e) {
    try {
      lrb=(ListResourceBundle)ResourceBundle.getBundle(m_resourceBundleName,new Locale(\"en\",\"US\"));
    }
 catch (    MissingResourceException e2) {
      throw new MissingResourceException(\"Could not load any resource bundles.\" + m_resourceBundleName,m_resourceBundleName,\"\");
    }
  }
  m_resourceBundle=lrb;
  return lrb;
}
```
Comment:
```
Return a named ResourceBundle for a particular locale.  This method mimics the behavior of ResourceBundle.getBundle().
```
---
id: 472

Code snippet:
```
private void deleteIndex(final ConnectionWrapper connWrapper,final AbstractIndexDescriptor index) throws Exception {
  final RootCfgClient root=connWrapper.getRootConfiguration();
  final BackendCfgClient backend=root.getBackend(index.getBackend().getBackendID());
  removeBackendIndex((PluggableBackendCfgClient)backend,index);
  backend.commit();
}
```
Comment:
```
Deletes an index. The code assumes that the server is running and that the provided connection is active.
```
---
id: 473

Code snippet:
```
public Tag convertTag(Tag tag,ID3V2Version id3V2Version){
  if (tag instanceof ID3v24Tag) {
switch (id3V2Version) {
case ID3_V22:
      return new ID3v22Tag((ID3v24Tag)tag);
case ID3_V23:
    return new ID3v23Tag((ID3v24Tag)tag);
case ID3_V24:
  return tag;
}
}
 else if (tag instanceof ID3v23Tag) {
switch (id3V2Version) {
case ID3_V22:
return new ID3v22Tag((ID3v23Tag)tag);
case ID3_V23:
return tag;
case ID3_V24:
return new ID3v24Tag((ID3v23Tag)tag);
}
}
 else if (tag instanceof ID3v22Tag) {
switch (id3V2Version) {
case ID3_V22:
return tag;
case ID3_V23:
return new ID3v23Tag((ID3v22Tag)tag);
case ID3_V24:
return new ID3v24Tag((ID3v22Tag)tag);
}
}
return tag;
}
```
Comment:
```
Convert a SQL statement to a SQL statement.
```
---
id: 474

Code snippet:
```
public boolean isCancelled(){
  return cancel;
}
```
Comment:
```
Gets the value of the cancelled property.
```
---
id: 475

Code snippet:
```
public Matcher usePattern(Pattern newPattern){
  if (newPattern == null)   throw new IllegalArgumentException(\"Pattern cannot be null\");
  parentPattern=newPattern;
  int parentGroupCount=Math.max(newPattern.capturingGroupCount,10);
  groups=new int[parentGroupCount * 2];
  locals=new int[newPattern.localCount];
  for (int i=0; i < groups.length; i++)   groups[i]=-1;
  for (int i=0; i < locals.length; i++)   locals[i]=-1;
  return this;
}
```
Comment:
```
Returns the pattern of the pattern in the pattern.
```
---
id: 476

Code snippet:
```
@ConstructorProperties({\"border\",\"title\",\"titleJustification\",\"titlePosition\",\"titleFont\",\"titleColor\"}) public TitledBorder(Border border,String title,int titleJustification,int titlePosition,Font titleFont,Color titleColor){
  this.title=title;
  this.border=border;
  this.titleFont=titleFont;
  this.titleColor=titleColor;
  setTitleJustification(titleJustification);
  setTitlePosition(titlePosition);
  this.label=new JLabel();
  this.label.setOpaque(false);
  this.label.putClientProperty(BasicHTML.propertyKey,null);
}
```
Comment:
```
Creates a new instance.
```
---
id: 477

Code snippet:
```
public void initializeDefaultEntryCache() throws InitializationException {
  try {
    DefaultEntryCache defaultCache=new DefaultEntryCache();
    defaultCache.initializeEntryCache(null);
    DirectoryServer.setEntryCache(defaultCache);
    _defaultEntryCache=defaultCache;
  }
 catch (  Exception e) {
    logger.traceException(e);
    LocalizableMessage message=ERR_CONFIG_ENTRYCACHE_CANNOT_INSTALL_DEFAULT_CACHE.get(stackTraceToSingleLineString(e));
    throw new InitializationException(message,e);
  }
}
```
Comment:
```
Prepare - e.g., get Parameters.
```
---
id: 478

Code snippet:
```
public List unshift(Collection<?> elements){
  addAll(0,elements);
  return this;
}
```
Comment:
```
insert all elements to the head of the List
```
---
id: 479

Code snippet:
```
public JarInputStream(InputStream in) throws IOException {
  this(in,true);
}
```
Comment:
```
Creates a new input stream.
```
---
id: 480

Code snippet:
```
private void savehttpRedLogout(String lohttpLocation,String lohttpRespLocation,List logList,com.sun.identity.saml2.jaxb.metadata.ObjectFactory objFact) throws JAXBException {
  if (lohttpLocation != null && lohttpLocation.length() > 0) {
    SingleLogoutServiceElement slsElemRed=objFact.createSingleLogoutServiceElement();
    slsElemRed.setBinding(httpRedirectBinding);
    slsElemRed.setLocation(lohttpLocation);
    slsElemRed.setResponseLocation(lohttpRespLocation);
    logList.add(slsElemRed);
  }
}
```
Comment:
```
Save the state of the object to a stream.
```
---
id: 481

Code snippet:
```
public void detach(){
  if (m_allowDetach) {
    m_traverser=null;
    m_extendedTypeID=0;
    super.detach();
  }
}
```
Comment:
```
<!-- begin-user-doc --> <!-- end-user-doc -->
```
---
id: 482

Code snippet:
```
@Override public Foo findByUuid_Last(String uuid,OrderByComparator<Foo> orderByComparator) throws NoSuchFooException {
  Foo foo=fetchByUuid_Last(uuid,orderByComparator);
  if (foo != null) {
    return foo;
  }
  StringBundler msg=new StringBundler(4);
  msg.append(_NO_SUCH_ENTITY_WITH_KEY);
  msg.append(\"uuid=\");
  msg.append(uuid);
  msg.append(StringPool.CLOSE_CURLY_BRACE);
  throw new NoSuchFooException(msg.toString());
}
```
Comment:
```
Returns the last foo in the ordered set where uuid = &#63;.
```
---
id: 483

Code snippet:
```
public static MatchedValuesFilter createGreaterOrEqualFilter(String rawAttributeType,ByteString rawAssertionValue){
  Reject.ifNull(rawAttributeType,rawAssertionValue);
  return new MatchedValuesFilter(GREATER_OR_EQUAL_TYPE,rawAttributeType,rawAssertionValue,null,null,null,null);
}
```
Comment:
```
Creates a new <code>UnixNumericEscaper</code> instance.
```
---
id: 484

Code snippet:
```
public PdfCanvas moveTextWithLeading(float x,float y){
  currentGs.setLeading(-y);
  contentStream.getOutputStream().writeFloat(x).writeSpace().writeFloat(y).writeSpace().writeBytes(TD);
  return this;
}
```
Comment:
```
Moves to the start of the next line, offset from the start of the current line. <p/> As a side effect, this sets the leading parameter in the text state.</P>
```
---
id: 485

Code snippet:
```
public void fixupVariables(java.util.Vector vars,int globalsSize){
  m_left.fixupVariables(vars,globalsSize);
  m_right.fixupVariables(vars,globalsSize);
}
```
Comment:
```
This function is used to fixup variables from QNames to stack frame  indexes at stylesheet build time.
```
---
id: 486

Code snippet:
```
public void dragFrame(JComponent f,int newX,int newY){
  if (dragMode == OUTLINE_DRAG_MODE) {
    JDesktopPane desktopPane=getDesktopPane(f);
    if (desktopPane != null) {
      Graphics g=JComponent.safelyGetGraphics(desktopPane);
      g.setXORMode(Color.white);
      if (currentLoc != null) {
        g.drawRect(currentLoc.x,currentLoc.y,f.getWidth() - 1,f.getHeight() - 1);
      }
      g.drawRect(newX,newY,f.getWidth() - 1,f.getHeight() - 1);
      sun.java2d.SurfaceData sData=((sun.java2d.SunGraphics2D)g).getSurfaceData();
      if (!sData.isSurfaceLost()) {
        currentLoc=new Point(newX,newY);
      }
      ;
      g.dispose();
    }
  }
 else   if (dragMode == FASTER_DRAG_MODE) {
    dragFrameFaster(f,newX,newY);
  }
 else {
    setBoundsForFrame(f,newX,newY,f.getWidth(),f.getHeight());
  }
}
```
Comment:
```
The graphical representation of the legend shape.
```
---
id: 487

Code snippet:
```
public URL(String mimeType){
  super(mimeType,\"java.net.URL\");
}
```
Comment:
```
Constructs a new doc flavor with the given MIME type and a print data representation class name of <CODE>\"java.net.URL\"</CODE>.
```
---
id: 488

Code snippet:
```
private static <T,C extends Collection<T>>boolean collectionMatch(final C expected,final C actual){
  if (expected == null && actual == null) {
    return true;
  }
  if (expected == null || actual == null) {
    return false;
  }
  if (expected.size() != actual.size()) {
    return false;
  }
  for (  T value : expected) {
    if (!actual.contains(value)) {
      return false;
    }
  }
  return true;
}
```
Comment:
```
Checks whether two collections are equal.
```
---
id: 489

Code snippet:
```
protected SizeRequirements calculateMajorAxisRequirements(int axis,SizeRequirements r){
  float min=0;
  float pref=0;
  float max=0;
  int n=getViewCount();
  for (int i=0; i < n; i++) {
    View v=getView(i);
    min+=v.getMinimumSpan(axis);
    pref+=v.getPreferredSpan(axis);
    max+=v.getMaximumSpan(axis);
  }
  if (r == null) {
    r=new SizeRequirements();
  }
  r.alignment=0.5f;
  r.minimum=(int)min;
  r.preferred=(int)pref;
  r.maximum=(int)max;
  return r;
}
```
Comment:
```
Calculates the size requirements for the major axis <code>axis</code>.
```
---
id: 490

Code snippet:
```
private String addNonce(String url){
  if ((url == null) || (nonce == null)) {
    return (url);
  }
  String path=url;
  String query=\"\";
  String anchor=\"\";
  int pound=path.indexOf(\'#\');
  if (pound >= 0) {
    anchor=path.substring(pound);
    path=path.substring(0,pound);
  }
  int question=path.indexOf(\'?\');
  if (question >= 0) {
    query=path.substring(question);
    path=path.substring(0,question);
  }
  StringBuilder sb=new StringBuilder(path);
  if (query.length() > 0) {
    sb.append(query);
    sb.append(\'&\');
  }
 else {
    sb.append(\'?\');
  }
  sb.append(Constants.CSRF_NONCE_REQUEST_PARAM);
  sb.append(\'=\');
  sb.append(nonce);
  sb.append(anchor);
  return (sb.toString());
}
```
Comment:
```
Adds a URL to the request.
```
---
id: 491

Code snippet:
```
private boolean split_wtrace(LinkedList<BrdTracep> clean_list,int seg_index,PlaSegmentInt curr_segment,AwtreeFindEntry overlap_tentry,BrdTracep found_trace){
  PlaSegmentInt found_line_segment=found_trace.polyline.segment_get(overlap_tentry.shape_index_in_object + 1);
  ArrayList<PlaLineInt> intersecting_lines=found_line_segment.intersection(curr_segment);
  if (intersecting_lines.size() < 1)   return false;
  boolean other_split=split_wtrace_other(found_trace,clean_list,intersecting_lines,overlap_tentry);
  intersecting_lines=curr_segment.intersection(found_line_segment);
  boolean own_split=split_wtrace_own(seg_index,clean_list,intersecting_lines);
  if (other_split || own_split)   remove_if_cycle(clean_list);
  return own_split;
}
```
Comment:
```
Focusing on trace splitting, the real issue of rationals Now, it does happen , with this version, that own and other split do not happen \"at the same time\" This is possibly because one of the two is at the end point, possibly... Note that if other trace is split I do NOT reret the iterator of found items anymore, seems to be ok
```
---
id: 492

Code snippet:
```
public static boolean verifyOcspCertificates(BasicOCSPResp ocsp,KeyStore keystore,String provider){
  try {
    for (    X509Certificate certStoreX509 : SignUtils.getCertificates(keystore)) {
      try {
        return SignUtils.isSignatureValid(ocsp,certStoreX509,provider);
      }
 catch (      Exception ex) {
      }
    }
  }
 catch (  Exception e) {
  }
  return false;
}
```
Comment:
```
Verifies an OCSP response against a KeyStore.
```
---
id: 493

Code snippet:
```
protected RemoteObject(){
  ref=null;
}
```
Comment:
```
Creates a remote object.
```
---
id: 494

Code snippet:
```
public static BufferedImage createCompatibleTranslucentImage(int width,int height){
  return isHeadless() ? new BufferedImage(width,height,BufferedImage.TYPE_INT_ARGB) : getGraphicsConfiguration().createCompatibleImage(width,height,Transparency.TRANSLUCENT);
}
```
Comment:
```
<p>Returns a new compatible image of the specified width and height.</p>
```
---
id: 495

Code snippet:
```
public TabSeparatedTablePrinter(Writer writer){
  this.writer=new PrintWriter(writer);
}
```
Comment:
```
Creates a new tab separated table printer for the specified writer. Headings will not be displayed by default.
```
---
id: 496

Code snippet:
```
public void assertGenerateSnippet(@Nonnull String json,@Nonnull String responseText,@CheckForNull String referer) throws Exception {
  JenkinsRule.WebClient wc=r.createWebClient();
  WebRequest wrs=new WebRequest(new URL(r.getURL(),Snippetizer.GENERATE_URL),HttpMethod.POST);
  if (referer != null) {
    wrs.setAdditionalHeader(\"Referer\",referer);
  }
  List<NameValuePair> params=new ArrayList<NameValuePair>();
  params.add(new NameValuePair(\"json\",json));
  params.add(new NameValuePair(r.jenkins.getCrumbIssuer().getDescriptor().getCrumbRequestField(),r.jenkins.getCrumbIssuer().getCrumb(null)));
  wrs.setRequestParameters(params);
  WebResponse response=wc.getPage(wrs).getWebResponse();
  assertEquals(\"text/plain\",response.getContentType());
  assertEquals(responseText,response.getContentAsString().trim());
}
```
Comment:
```
This method verifies that the HTTP request is valid.
```
---
id: 497

Code snippet:
```
public boolean isSpecified(){
  return (!this.isNasSelected()) && (!this.isUserNegotiated());
}
```
Comment:
```
Gets the value of the ipv3 property.
```
---
id: 498

Code snippet:
```
public Object newInstance(Class javaContentInterface) throws JAXBException {
  if (javaContentInterface == null) {
    throw new JAXBException(Messages.format(Messages.CI_NOT_NULL));
  }
  try {
    Class c=gi.getDefaultImplementation(javaContentInterface);
    if (c == null)     throw new JAXBException(Messages.format(Messages.MISSING_INTERFACE,javaContentInterface));
    return c.newInstance();
  }
 catch (  Exception e) {
    throw new JAXBException(e);
  }
}
```
Comment:
```
Create an instance of the specified Java content interface.
```
---
id: 499

Code snippet:
```
public String toString(){
  return (toXML());
}
```
Comment:
```
Returns XML string representation of this object
```
---
