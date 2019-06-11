id: 300

Code snippet:
```
int CountRange(int NumofGlyphs,int Type){
  int num=0;
  char Sid;
  int i=1, nLeft;
  while (i < NumofGlyphs) {
    num++;
    Sid=getCard16();
    if (Type == 1)     nLeft=getCard8();
 else     nLeft=getCard16();
    i+=nLeft + 1;
  }
  return num;
}
```
Comment:
```
Returns the number of characters in the given range.
```
---
id: 301

Code snippet:
```
public void printStackTrace(){
  printStackTrace(new java.io.PrintWriter(System.err,true));
}
```
Comment:
```
Print the the trace of methods from where the error originated. this will trace all nested exception objects, as well as this object.
```
---
id: 302

Code snippet:
```
private void updateDNValue(){
  String attr=(String)namingAttribute.getSelectedItem();
  for (int i=0; i < NAMING_ATTRIBUTE_TEXTFIELDS.length; i++) {
    if (attr.equalsIgnoreCase(NAMING_ATTRIBUTES[i])) {
      String value=NAMING_ATTRIBUTE_TEXTFIELDS[i].getText().trim();
      dn.setText(attr + \"=\" + value+ \",\"+ parentNode.getDN());
      break;
    }
  }
}
```
Comment:
```
Updates the property.
```
---
id: 303

Code snippet:
```
@BeforeClass public void startServer() throws Exception {
  TestCaseUtils.startServer();
}
```
Comment:
```
Starts the server.
```
---
id: 304

Code snippet:
```
public PdfADocument(PdfWriter writer,PdfAConformanceLevel conformanceLevel,PdfOutputIntent outputIntent){
  super(writer);
  setChecker(conformanceLevel);
  addOutputIntent(outputIntent);
}
```
Comment:
```
Creates a new instance of the given data.
```
---
id: 305

Code snippet:
```
public FrameBodyTSRC(byte textEncoding,String text){
  super(textEncoding,text);
}
```
Comment:
```
Creates a new instance of the given class.
```
---
id: 306

Code snippet:
```
private static int lastIndexOf(Object o,Object[] elements,int index){
  if (o == null) {
    for (int i=index; i >= 0; i--)     if (elements[i] == null)     return i;
  }
 else {
    for (int i=index; i >= 0; i--)     if (o.equals(elements[i]))     return i;
  }
  return -1;
}
```
Comment:
```
Returns the index of the specified element in the specified element.
```
---
id: 307

Code snippet:
```
public XMLFilterImpl(XMLReader parent){
  setParent(parent);
}
```
Comment:
```
Construct an xml filter with the specified parent.
```
---
id: 308

Code snippet:
```
@Override public int hashCode(){
  int hash=5;
  hash=59 * hash + Objects.hashCode(this.name);
  hash=59 * hash + Objects.hashCode(this.description);
  return hash;
}
```
Comment:
```
Returns a hash code for this object.
```
---
id: 309

Code snippet:
```
public void testPowNegativeNumToEvenExp(){
  byte aBytes[]={50,-26,90,69,120,32,63,-103,-14,35};
  int aSign=-1;
  int exp=4;
  byte rBytes[]={102,107,-122,-43,-52,-20,-27,25,-9,88,-13,75,78,81,-33,-77,39,27,-37,106,121,-73,108,-47,-101,80,-25,71,13,94,-7,-33,1,-17,-65,-70,-61,-3,-47};
  BigInteger aNumber=new BigInteger(aSign,aBytes);
  BigInteger result=aNumber.pow(exp);
  byte resBytes[]=new byte[rBytes.length];
  resBytes=result.toByteArray();
  for (int i=0; i < resBytes.length; i++) {
    assertTrue(resBytes[i] == rBytes[i]);
  }
  assertEquals(\"incorrect sign\",1,result.signum());
}
```
Comment:
```
New bigdecimal(int n) from a positive number.
```
---
id: 310

Code snippet:
```
public static boolean startupCalled(){
  return startupCalled;
}
```
Comment:
```
Indicates whether the server startup plugins have been called.
```
---
id: 311

Code snippet:
```
public static void sendAlertNotification(AlertGenerator generator,String alertType,LocalizableMessage alertMessage){
  DirectoryServer.sendAlertNotification(generator,alertType,alertMessage);
}
```
Comment:
```
Sends an alert notification with the provided information.
```
---
id: 312

Code snippet:
```
public synchronized void mark(int readlimit){
  marklimit=readlimit;
  markpos=pos;
}
```
Comment:
```
Marks the current position.
```
---
id: 313

Code snippet:
```
public boolean isDefaultButton(){
  JRootPane root=SwingUtilities.getRootPane(this);
  if (root != null) {
    return root.getDefaultButton() == this;
  }
  return false;
}
```
Comment:
```
Returns true if the component has changed.
```
---
id: 314

Code snippet:
```
public static Cookie createCookie(String cookieValue,String cookieDomain){
  String cookieName=getCookieName();
  if (utilDebug.messageEnabled()) {
    utilDebug.message(\"cookieName=\'{}\', cookieValue=\'{}\', cookieDomain=\'{}\'\",cookieName,cookieValue,cookieDomain);
  }
  return (createCookie(cookieName,cookieValue,cookieDomain));
}
```
Comment:
```
Returns cookie to be set in the response.
```
---
id: 315

Code snippet:
```
public void resumeEncoding(){
  this.suspendEncoding=false;
}
```
Comment:
```
Resumes encoding of the stream. may be helpful if you need to embed a piece of base640-encoded data in a stream.
```
---
id: 316

Code snippet:
```
public int plaline_len(){
  return lines_list.size();
}
```
Comment:
```
Replacement for getting len instead of using direct array.
```
---
id: 317

Code snippet:
```
private void seekStation(final int station,boolean direction){
  startAnimation();
  refreshImageButton(false);
  refreshActionMenuItem(false);
  refreshPopupMenuItem(false);
  refreshActionMenuPower(false);
  mService.seekStationAsync(FmRadioUtils.computeFrequency(station),direction);
}
```
Comment:
```
Seek station according current frequency and direction.
```
---
id: 318

Code snippet:
```
private void reportInterruptAfterWait(int interruptMode) throws InterruptedException {
  if (interruptMode == THROW_IE)   throw new InterruptedException();
 else   if (interruptMode == REINTERRUPT)   selfInterrupt();
}
```
Comment:
```
Throws interruptedexception, reinterrupts current thread, or does nothing, depending on mode.
```
---
id: 319

Code snippet:
```
@Override public void addRuleInstances(Digester digester){
  digester.addRule(prefix + \"user\",new MemoryUserRule());
}
```
Comment:
```
Adds a new rule to the current state.
```
---
id: 320

Code snippet:
```
public com.sun.identity.liberty.ws.common.jaxb.xmlsig.SignedInfoElement createSignedInfoElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.liberty.ws.common.jaxb.xmlsig.impl.SignedInfoElementImpl();
}
```
Comment:
```
Create an instance of signedinfoelement.
```
---
id: 321

Code snippet:
```
public com.sun.identity.saml2.jaxb.xmlenc.ReferenceListType.KeyReference createReferenceListTypeKeyReference() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.saml2.jaxb.xmlenc.impl.ReferenceListTypeImpl.KeyReferenceImpl();
}
```
Comment:
```
Create an instance of referencelisttypekeyreference.
```
---
id: 322

Code snippet:
```
private void initData(Context context){
  scroller=new WheelScroller(getContext(),scrollingListener);
  mPaintLineCenter=new Paint();
  mPaintLineCenter.setColor(DefaultConfig.COLOR);
  mPaintLineCenter.setAntiAlias(true);
  mPaintLineCenter.setStrokeWidth(1);
  mPaintLineCenter.setStyle(Paint.Style.FILL);
  mPaintLineRight=new Paint();
  mPaintLineRight.setColor(0xffe8e8e8);
  mPaintLineRight.setAntiAlias(true);
  mPaintLineRight.setStrokeWidth(1);
  mPaintLineRight.setStyle(Paint.Style.FILL);
  mPaintRectCenter=new Paint();
  mPaintRectCenter.setColor(DefaultConfig.COLOR);
  mPaintRectCenter.setAlpha((int)(0.1 * 255));
  mPaintRectCenter.setAntiAlias(true);
  mPaintRectCenter.setStyle(Paint.Style.FILL);
  mLineRightMar=context.getResources().getDimensionPixelSize(R.dimen.picker_line_mar);
  defaultColor=DefaultConfig.TV_NORMAL_COLOR;
  selectorColor=DefaultConfig.TV_SELECTOR_COLOR;
}
```
Comment:
```
Initializes the panel.
```
---
id: 323

Code snippet:
```
@Override public synchronized void clear(){
  if (null != factory) {
    final Iterator<PooledSoftReference<T>> iter=idleReferences.iterator();
    while (iter.hasNext()) {
      try {
        final PooledSoftReference<T> ref=iter.next();
        if (null != ref.getObject()) {
          factory.destroyObject(ref);
        }
      }
 catch (      final Exception e) {
      }
    }
  }
  idleReferences.clear();
  pruneClearedReferences();
}
```
Comment:
```
Clears the cache.
```
---
id: 324

Code snippet:
```
public SAMLToken(String primaryKey,String secondaryKey,long expiryTime,Object token){
  this.primaryKey=primaryKey;
  this.secondaryKey=secondaryKey;
  this.expiryTime=expiryTime;
  this.token=token;
}
```
Comment:
```
Create a new instance of the samltoken.
```
---
id: 325

Code snippet:
```
public String encode(){
  return encode(new StringBuilder()).toString();
}
```
Comment:
```
Returns a string representation of this object.
```
---
id: 326

Code snippet:
```
public boolean isFileHidingEnabled(){
  return useFileHiding;
}
```
Comment:
```
Returns true if the current state is enabled.
```
---
id: 327

Code snippet:
```
private void fireMenuKeyReleased(MenuKeyEvent event){
  Object[] listeners=listenerList.getListenerList();
  for (int i=listeners.length - 2; i >= 0; i-=2) {
    if (listeners[i] == MenuKeyListener.class) {
      ((MenuKeyListener)listeners[i + 1]).menuKeyReleased(event);
    }
  }
}
```
Comment:
```
Notifies all listeners that have registered interest for notification on this event type.
```
---
id: 328

Code snippet:
```
public static Message sendRequest(Message req,String connectTo) throws SOAPBindingException, SOAPFaultException {
  return sendRequest(req,connectTo,null,null);
}
```
Comment:
```
Sends a request to a soap endpoint and returns the response. the server only contains one servlet for different web services. so the soap endpoint url has format \'servlet_url/key\'.
```
---
id: 329

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
Comment:
```
Cleanup the whole junit scenario ; deletes the created git repository.
```
---
id: 330

Code snippet:
```
public KeyGenerationParameters(SecureRandom random,int strength){
  this.random=random;
  this.strength=strength;
}
```
Comment:
```
Initialise the generator with a source of randomness and a strength (in bits).
```
---
id: 331

Code snippet:
```
public static Map<String,Set<String>> cloneMap(Map<String,Set<String>> map){
  Map<String,Set<String>> clone=new HashMap<String,Set<String>>();
  for (  String key : map.keySet()) {
    Set<String> set=new HashSet<String>();
    Set<String> orig=(Set<String>)map.get(key);
    set.addAll(orig);
    clone.put(key,set);
  }
  return clone;
}
```
Comment:
```
Returns a cloned map of string to set of string.
```
---
id: 332

Code snippet:
```
public FrameBodyTDRC(FrameBodyTIME body){
  originalID=ID3v23Frames.FRAME_ID_V3_TIME;
  time=body.getText();
  setHoursOnly(body.isHoursOnly());
  setObjectValue(DataTypes.OBJ_TEXT_ENCODING,TextEncoding.ISO_8859_1);
  setObjectValue(DataTypes.OBJ_TEXT,getFormattedText());
}
```
Comment:
```
Creates a new instance.
```
---
id: 333

Code snippet:
```
private void appendNodeValue(String value,boolean forAttribute) throws IOException {
  if (value == null) {
    value=\"\";
  }
  write(Utils.escapeXML(value,forAttribute,true));
}
```
Comment:
```
Serializes the node value in xml encoding. its used for tag bodies and attributes. <em>note:</em> the attribute is always limited by quotes, thats why <code>&amp;apos;</code> is never serialized. <em>note:</em> control chars are written unescaped, but if the user uses others than tab, lf and cr the resulting xml will become invalid.
```
---
id: 334

Code snippet:
```
public com.sun.identity.saml2.jaxb.assertion.ActionElement createActionElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.saml2.jaxb.assertion.impl.ActionElementImpl();
}
```
Comment:
```
Create an instance of actionelement.
```
---
id: 335

Code snippet:
```
public boolean validateFileFormat(Path location,Configuration conf){
  FileSystem fileSystem;
  try {
    fileSystem=FileSystem.get(location.toUri(),conf);
    FileStatus[] items=fileSystem.listStatus(location);
    for (    FileStatus item : items) {
      if (item.getPath().getName().startsWith(\"_\")) {
        continue;
      }
 else       if (item.getPath().getName().contains(\".avro\")) {
        logger.debug(item.getPath().getName());
        logger.info(\"Created File format is AVRO !\");
        return true;
      }
 else       logger.debug(item.getPath().getName());
      logger.error(\"Created File Format is not correct\");
    }
  }
 catch (  IOException e) {
    logger.trace(e.getMessage());
  }
  return false;
}
```
Comment:
```
This method is to validate the file format. it will return true when file format is avro else it will return false.
```
---
id: 336

Code snippet:
```
public JScrollBar createHorizontalScrollBar(){
  return new ScrollBar(JScrollBar.HORIZONTAL);
}
```
Comment:
```
Returns a <code>jscrollpane.scrollbar</code> by default. subclasses may override this method to force <code>scrollpaneui</code> implementations to use a <code>jscrollbar</code> subclass. used by <code>scrollpaneui</code> implementations to create the horizontal scrollbar.
```
---
id: 337

Code snippet:
```
public MidiEvent(MidiMessage message,long tick){
  this.message=message;
  this.tick=tick;
}
```
Comment:
```
Constructs a new <code>midievent</code>.
```
---
id: 338

Code snippet:
```
public Object[] toArray(){
  final ReentrantLock lock=this.lock;
  lock.lock();
  try {
    return q.toArray();
  }
  finally {
    lock.unlock();
  }
}
```
Comment:
```
Returns an array containing all of the elements in this queue. the returned array elements are in no particular order. <p>the returned array will be \"safe\" in that no references to it are maintained by this queue. (in other words, this method must allocate a new array). the caller is thus free to modify the returned array. <p>this method acts as bridge between array-based and collection-based apis.
```
---
id: 339

Code snippet:
```
private void abortOnSSLException() throws IOException {
  if (sslException != null) {
    throw sslException;
  }
}
```
Comment:
```
Throws an exception.
```
---
id: 340

Code snippet:
```
public static Properties readPropertiesFile(final File file){
  if (!file.exists()) {
    JKIOUtil.logger.info(String.format(\"File %s doesnot exists , return empty map\",file.getName()));
    return new Properties();
  }
  try {
    InputStream in=new FileInputStream(file);
    if (in != null) {
      return readPropertiesStream(in);
    }
  }
 catch (  IOException e) {
    JKExceptionUtil.handle(e);
  }
  return null;
}
```
Comment:
```
Read a file.
```
---
id: 341

Code snippet:
```
public Shape modelToView(int pos,Shape a,Position.Bias b) throws BadLocationException {
  if (!isAllocationValid()) {
    Rectangle alloc=a.getBounds();
    setSize(alloc.width,alloc.height);
  }
  return super.modelToView(pos,a,b);
}
```
Comment:
```
Provides a mapping from the document model coordinate space to the coordinate space of the view mapped to it. this makes sure the allocation is valid before calling the superclass.
```
---
id: 342

Code snippet:
```
public java.lang.Object newInstance(java.lang.Class javaContentInterface) throws javax.xml.bind.JAXBException {
  return super.newInstance(javaContentInterface);
}
```
Comment:
```
Create an instance of the specified java content interface.
```
---
id: 343

Code snippet:
```
public boolean isResourceNameAllowed(){
  return (isResourceNameAllowed);
}
```
Comment:
```
Checks if the attribute allows to have resource name.
```
---
id: 344

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList elementList;
  Node nameNode;
  CharacterData child;
  String childData;
  doc=(Document)load(\"staff\",true);
  elementList=doc.getElementsByTagName(\"address\");
  nameNode=elementList.item(0);
  child=(CharacterData)nameNode.getFirstChild();
  child.replaceData(30,5,\"98665\");
  childData=child.getData();
  assertEquals(\"characterdataReplaceDataEndAssert\",\"1230 North Ave. Dallas, Texas 98665\",childData);
}
```
Comment:
```
Runs the test case.
```
---
id: 345

Code snippet:
```
public ObjectStack(int blocksize){
  super(blocksize);
}
```
Comment:
```
Creates a new <code>object</code> object.
```
---
id: 346

Code snippet:
```
public boolean isUnderflow(){
  return this.type == TYPE_UNDERFLOW;
}
```
Comment:
```
Returns true if the given value is null.
```
---
id: 347

Code snippet:
```
public int count(){
  return padstack_list.size();
}
```
Comment:
```
Returns the count of padstacks in this object.
```
---
id: 348

Code snippet:
```
@Override public final boolean isEnabled(){
  return isEnabled;
}
```
Comment:
```
Gets the value of this property.
```
---
id: 349

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList elementList;
  Node employeeNode;
  NodeList childList;
  Node oldChild;
  Node removedChild;
  String childName;
  String oldName;
  doc=(Document)load(\"hc_staff\",true);
  elementList=doc.getElementsByTagName(\"p\");
  employeeNode=elementList.item(1);
  childList=employeeNode.getChildNodes();
  oldChild=childList.item(0);
  oldName=oldChild.getNodeName();
  removedChild=employeeNode.removeChild(oldChild);
  assertNotNull(\"notnull\",removedChild);
  childName=removedChild.getNodeName();
  assertEquals(\"nodeName\",oldName,childName);
}
```
Comment:
```
Runs the test case.
```
---
id: 350

Code snippet:
```
public boolean show(Container c,int x,int y,int w,int h){
  return false;
}
```
Comment:
```
Shows a region of a previously rendered component. this will return true if successful, false otherwise. the default implementation returns false.
```
---
id: 351

Code snippet:
```
public boolean equals(Object object){
  return (super.equals(object) && object instanceof RequestingUserName);
}
```
Comment:
```
Returns whether this requesting user name attribute is equivalent to the passed in object. to be equivalent, all of the following conditions must be true: <ol type=1> <li> <code>object</code> is not null. <li> <code>object</code> is an instance of class requestingusername. <li> this requesting user name attribute\'s underlying string and <code>object</code>\'s underlying string are equal. <li> this requesting user name attribute\'s locale and <code>object</code>\'s locale are equal. </ol>.
```
---
id: 352

Code snippet:
```
public Set createAssignableDynamicGroups(Set groupNames) throws AMException, SSOException {
  Iterator iter=groupNames.iterator();
  Set groups=new HashSet();
  while (iter.hasNext()) {
    String groupDN=AMNamingAttrManager.getNamingAttr(GROUP) + \"=\" + ((String)iter.next())+ \",\"+ super.entryDN;
    AMAssignableDynamicGroupImpl groupImpl=new AMAssignableDynamicGroupImpl(super.token,groupDN);
    groupImpl.create();
    groups.add(groupImpl);
  }
  return groups;
}
```
Comment:
```
Creates assignable dynamic groups in this group.
```
---
id: 353

Code snippet:
```
private Object readResolve(){
  return object;
}
```
Comment:
```
Ensures that the given object is the same as an object.
```
---
id: 354

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(hc_entitiesremovenameditemns1.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 355

Code snippet:
```
public RSInfo(int rsServerId,String rsServerURL,long generationId,byte groupId,int weight){
  this.rsServerId=rsServerId;
  this.rsServerURL=rsServerURL;
  this.generationId=generationId;
  this.groupId=groupId;
  this.weight=weight;
}
```
Comment:
```
Creates a new instance.
```
---
id: 356

Code snippet:
```
public KeyBinding(KeyStroke key,String actionName){
  this.key=key;
  this.actionName=actionName;
}
```
Comment:
```
Creates a new instance.
```
---
id: 357

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
Comment:
```
Runs the test case.
```
---
id: 358

Code snippet:
```
private void updateRingColor(float interpolatedTime,Ring ring){
  if (interpolatedTime > COLOR_START_DELAY_OFFSET) {
    ring.setColor(evaluateColorChange((interpolatedTime - COLOR_START_DELAY_OFFSET) / (1.0f - COLOR_START_DELAY_OFFSET),ring.getStartingColor(),ring.getNextColor()));
  }
}
```
Comment:
```
Update the ring color if this is within the last 25% of the animation. the new ring color will be a translation from the starting ring color to the next color.
```
---
id: 359

Code snippet:
```
public Panel(LayoutManager layout){
  setLayout(layout);
}
```
Comment:
```
Creates a new panel with the specified layout manager.
```
---
id: 360

Code snippet:
```
public RegexFileFilter(String pattern,int flags){
  if (pattern == null) {
    throw new IllegalArgumentException(\"Pattern is missing\");
  }
  this.pattern=Pattern.compile(pattern,flags);
}
```
Comment:
```
Creates a new <code>pattern</code>.
```
---
id: 361

Code snippet:
```
public AccountUsableResponseControl(boolean isInactive,boolean isReset,boolean isExpired,int remainingGraceLogins,boolean isLocked,int secondsBeforeUnlock){
  this(false,isInactive,isReset,isExpired,remainingGraceLogins,isLocked,secondsBeforeUnlock);
}
```
Comment:
```
Creates a new account usability response control that may be used to indicate that the account is not available and provide information about the underlying reason. it will use the default oid and criticality.
```
---
id: 362

Code snippet:
```
public void invoke(String invokeMethod,Marshallable param,ClientCallback clientCallback){
  TransactInfo transactInfo=TransactInfo.createDirectInvoke(invokeMethod);
  mClientProxy.transact(transactInfo,param,clientCallback);
}
```
Comment:
```
Invoke js_server method.
```
---
id: 363

Code snippet:
```
public String createHttpConnector(String parent,String address,int port) throws Exception {
  return createConnector(parent,address,port,false,false);
}
```
Comment:
```
Create a new httpconnector.
```
---
id: 364

Code snippet:
```
public void testIsSupported1() throws Throwable {
  Document doc;
  Node rootNode;
  boolean state;
  doc=(Document)load(\"staff\",builder);
  rootNode=doc.getDocumentElement();
  state=rootNode.isSupported(\"XXX\",\"1.0\");
  assertFalse(\"throw_False\",state);
}
```
Comment:
```
Runs the test case.
```
---
id: 365

Code snippet:
```
public boolean contains(JComponent a,int b,int c){
  boolean returnValue=((ComponentUI)(uis.elementAt(0))).contains(a,b,c);
  for (int i=1; i < uis.size(); i++) {
    ((ComponentUI)(uis.elementAt(i))).contains(a,b,c);
  }
  return returnValue;
}
```
Comment:
```
Invokes the <code>contains</code> method on each ui handled by this object.
```
---
id: 366

Code snippet:
```
public final void testGetType02(){
  CRL crl=new MyCRL(null);
  assertNull(crl.getType());
}
```
Comment:
```
Test #2 for <code>gettype()</code> method<br> assertion: returns <code>crl</code> type.
```
---
id: 367

Code snippet:
```
public void processAck(RequestEvent requestEvent,ServerTransaction serverTransaction){
  SipProvider sipProvider=(SipProvider)requestEvent.getSource();
  try {
    logger.info(\"shootme: got an ACK \" + requestEvent.getRequest());
    TestCase.assertTrue(\"dialog mismatch \",this.dialog == serverTransaction.getDialog());
    int ackCount=((ApplicationData)dialog.getApplicationData()).ackCount;
    if (ackCount == 1 && this.sendReInviteFlag) {
      dialog=inviteTid.getDialog();
      this.sendReInvite(sipProvider);
    }
 else     ((ApplicationData)dialog.getApplicationData()).ackCount++;
  }
 catch (  Exception ex) {
    String s=\"Unexpected error\";
    logger.error(s,ex);
    TestCase.fail(s);
  }
}
```
Comment:
```
Processes a message.
```
---
id: 368

Code snippet:
```
public GSERParser readEndSequence() throws DecodeException {
  skip(GSER_SP);
  next(GSER_SEQUENCE_END);
  return this;
}
```
Comment:
```
Skips the input matching the end of a sequence and preceding space characters.
```
---
id: 369

Code snippet:
```
public SIPHeader parse() throws ParseException {
  if (debug)   dbg_enter(\"RSeqParser.parse\");
  RSeq rseq=new RSeq();
  try {
    headerName(TokenTypes.RSEQ);
    rseq.setHeaderName(SIPHeaderNames.RSEQ);
    String number=this.lexer.number();
    try {
      rseq.setSeqNumber(Long.parseLong(number));
    }
 catch (    InvalidArgumentException ex) {
      throw createParseException(ex.getMessage());
    }
    this.lexer.SPorHT();
    this.lexer.match(\'
\');
    return rseq;
  }
  finally {
    if (debug)     dbg_leave(\"RSeqParser.parse\");
  }
}
```
Comment:
```
Parse the string message.
```
---
id: 370

Code snippet:
```
public boolean offerFirst(E e){
  addFirst(e);
  return true;
}
```
Comment:
```
Inserts the specified element at the front of this list.
```
---
id: 371

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(hc_characterdatadeletedatagetlengthanddata.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 372

Code snippet:
```
public static void marshal(Object jaxbObject,String xml){
  _marshal(jaxbObject,xml);
}
```
Comment:
```
Writes a java object tree to xml and store it to the specified location.
```
---
id: 373

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  Element element;
  Element child1;
  Element child2;
  Element child3;
  Node appendedChild;
  NodeList elementList;
  String nullNS=null;
  doc=(Document)load(\"staffNS\",false);
  element=doc.createElementNS(\"http://www.w3.org/DOM\",\"root\");
  child1=doc.createElementNS(\"http://www.w3.org/DOM/Level1\",\"dom:child\");
  child2=doc.createElementNS(nullNS,\"child\");
  child3=doc.createElementNS(\"http://www.w3.org/DOM/Level2\",\"dom:child\");
  appendedChild=element.appendChild(child1);
  appendedChild=element.appendChild(child2);
  appendedChild=element.appendChild(child3);
  elementList=element.getElementsByTagNameNS(nullNS,\"child\");
  assertSize(\"elementgetelementsbytagnamens04_1\",1,elementList);
  elementList=element.getElementsByTagNameNS(\"*\",\"child\");
  assertSize(\"elementgetelementsbytagnamens04_2\",3,elementList);
}
```
Comment:
```
Runs the test case.
```
---
id: 374

Code snippet:
```
public PrintWriter log(PrintWriter out){
  return log(this,out);
}
```
Comment:
```
Log the given output stream.
```
---
id: 375

Code snippet:
```
public boolean isChar(StringLiteral literal,LineCol lineCol,boolean testSymbol) throws SyntaxException {
  String str=literal.literal();
  str=str.substring(1);
  str=str.substring(0,str.length() - 1);
  if (testSymbol && !literal.literal().startsWith(\"\\'\"))   return false;
  String s=unescape(str,lineCol);
  assert s != null;
  return s.length() == 1;
}
```
Comment:
```
Checks if the given character is a string.
```
---
id: 376

Code snippet:
```
public Builder prohibitedAttributes(final String... attributeNamesOrOIDs){
  this.prohibitedAttributeOIDs.addAll(asList(attributeNamesOrOIDs));
  return this;
}
```
Comment:
```
Sets the attributes for the given property.
```
---
id: 377

Code snippet:
```
@Override protected void doPost(final HttpServletRequest request,final HttpServletResponse response) throws ServletException, IOException {
  request.setCharacterEncoding(\"UTF-8\");
  response.setCharacterEncoding(\"UTF-8\");
  getResponse(request,response,true);
}
```
Comment:
```
Process the http post request.
```
---
id: 378

Code snippet:
```
@Parameters({\"parent-realm\",\"entity-type\",\"entity-name\"}) @Test(groups={\"api\",\"memberships\"},expectedExceptions={IdRepoException.class}) public void addItselfAsMember(String parentRealm,String idType,String entityName) throws IdRepoException, SSOException {
  Object[] params={parentRealm,idType,entityName};
  entering(\"addItselfAsMember\",params);
  try {
    AMIdentity amid=getIdentity(parentRealm,IdUtils.getType(idType),entityName);
    amid.removeMember(amid);
  }
 catch (  SSOException e) {
    log(Level.SEVERE,\"addItselfAsMember\",e.getMessage(),params);
    e.printStackTrace();
    throw e;
  }
  exiting(\"addItselfAsMember\");
}
```
Comment:
```
Creates a new instance.
```
---
id: 379

Code snippet:
```
public static void initializeConfigurationFramework(){
  if (!ConfigurationFramework.getInstance().isInitialized()) {
    try {
      final Logger configFrameworkLogger=Logger.getLogger(\"com.forgerock.opendj.ldap.config.config\");
      configFrameworkLogger.setUseParentHandlers(false);
      ConfigurationFramework.getInstance().initialize();
      configFrameworkLogger.setUseParentHandlers(true);
    }
 catch (    ConfigException e) {
      final LocalizableMessage message=ERROR_CTRL_PANEL_INITIALIZE_CONFIG_OFFLINE.get(e.getLocalizedMessage());
      logger.error(message);
      throw new RuntimeException(message.toString(),e);
    }
  }
}
```
Comment:
```
Initializes the configuration file.
```
---
id: 380

Code snippet:
```
public Observable<Void> initializePersistenceObservable(){
  io.vertx.rx.java.ObservableFuture<Void> resultHandler=io.vertx.rx.java.RxHelper.observableFuture();
  initializePersistence(resultHandler.toHandler());
  return resultHandler;
}
```
Comment:
```
Initialize the persistence.
```
---
id: 381

Code snippet:
```
public boolean equals(Object object){
  return (object != null && object instanceof TextSyntax && this.value.equals(((TextSyntax)object).value) && this.locale.equals(((TextSyntax)object).locale));
}
```
Comment:
```
Returns true if the given object is equal to this object.
```
---
id: 382

Code snippet:
```
public AuthenticationInfo(Entry authenticationEntry,boolean isRoot){
  this.authenticationEntry=authenticationEntry;
  this.isRoot=isRoot;
  isAuthenticated=authenticationEntry != null;
  mustChangePassword=false;
  simpleBindDN=authenticationEntry != null ? authenticationEntry.getName() : null;
  authorizationEntry=authenticationEntry;
  saslMechanism=null;
  authenticationType=AuthenticationType.INTERNAL;
}
```
Comment:
```
Creates a new set of authentication information to be used for clients that are authenticated internally.
```
---
id: 383

Code snippet:
```
public boolean verify(SignerInformationVerifier verifier) throws CMSException {
  Time signingTime=getSigningTime();
  if (verifier.hasAssociatedCertificate()) {
    if (signingTime != null) {
      X509CertificateHolder dcv=verifier.getAssociatedCertificate();
      if (!dcv.isValidOn(signingTime.getDate())) {
        throw new CMSVerifierCertificateNotValidException(\"verifier not valid at signingTime\");
      }
    }
  }
  return doVerify(verifier);
}
```
Comment:
```
Returns true if the signature is a valid signature.
```
---
id: 384

Code snippet:
```
public void mouseWheelMoved(MouseWheelEvent e){
  getHandler().mouseWheelMoved(e);
}
```
Comment:
```
Called when the mouse wheel is rotated while over a jscrollpane.
```
---
id: 385

Code snippet:
```
public void handleButton2Request(RequestInvocationEvent event) throws ModelControlException {
  try {
    forwardToAMViewBean();
  }
 catch (  AMConsoleException e) {
    setInlineAlertMessage(CCAlert.TYPE_ERROR,\"message.error\",e.getMessage());
  }
}
```
Comment:
```
Handles cancel button request.
```
---
id: 386

Code snippet:
```
public static void serialize(XMPMetaImpl xmp,OutputStream output,SerializeOptions options) throws XMPException {
  options=options != null ? options : new SerializeOptions();
  if (options.getSort()) {
    xmp.sort();
  }
  new XMPSerializerRDF().serialize(xmp,output,options);
}
```
Comment:
```
Serializes the given element.
```
---
id: 387

Code snippet:
```
public void firePropertyChange(String propertyName,float oldValue,float newValue){
}
```
Comment:
```
Overridden for performance reasons. see the <a href=\"#override\">implementation note</a> for more information.
```
---
id: 388

Code snippet:
```
public GenericAgentProfileViewBean(){
  super(\"GenericAgentProfile\");
  setDefaultDisplayURL(DEFAULT_DISPLAY_URL);
}
```
Comment:
```
Creates an instance of this view bean.
```
---
id: 389

Code snippet:
```
protected void closeStartTag() throws SAXException {
  if (m_elemContext.m_startTagOpen) {
    try {
      if (m_tracer != null)       super.fireStartElem(m_elemContext.m_elementName);
      int nAttrs=m_attributes.getLength();
      if (nAttrs > 0) {
        processAttributes(m_writer,nAttrs);
        m_attributes.clear();
      }
      m_writer.write(\'>\');
    }
 catch (    IOException e) {
      throw new SAXException(e);
    }
    if (m_CdataElems != null)     m_elemContext.m_isCdataSection=isCdataSection();
    if (m_doIndent) {
      m_isprevtext=false;
      m_preserves.push(m_ispreserve);
    }
  }
}
```
Comment:
```
For the enclosing elements starting tag write out out any attributes followed by \">\".
```
---
id: 390

Code snippet:
```
public ID3v24Tag(ByteBuffer buffer,String loggingFilename) throws TagException {
  frameMap=new LinkedHashMap();
  encryptedFrameMap=new LinkedHashMap();
  setLoggingFilename(loggingFilename);
  this.read(buffer);
}
```
Comment:
```
Creates a new instance.
```
---
id: 391

Code snippet:
```
public boolean isTrustedProvider(String realm,String federationId,String trustedEntityId) throws WSFederationMetaException {
  boolean result=false;
  SPSSOConfigElement spconfig=getSPSSOConfig(realm,federationId);
  if (spconfig != null) {
    result=isSameCircleOfTrust(spconfig,realm,trustedEntityId);
  }
  if (result) {
    return true;
  }
  IDPSSOConfigElement idpconfig=getIDPSSOConfig(realm,federationId);
  if (idpconfig != null) {
    return (isSameCircleOfTrust(idpconfig,realm,trustedEntityId));
  }
  return false;
}
```
Comment:
```
Determines whether two entities are in the same circle of trust under the realm.
```
---
id: 392

Code snippet:
```
public static boolean isXML11ValidQName(String str){
  final int colon=str.indexOf(\':\');
  if (colon == 0 || colon == str.length() - 1) {
    return false;
  }
  if (colon > 0) {
    final String prefix=str.substring(0,colon);
    final String localPart=str.substring(colon + 1);
    return isXML11ValidNCName(prefix) && isXML11ValidNCName(localPart);
  }
 else {
    return isXML11ValidNCName(str);
  }
}
```
Comment:
```
Returns true if the given string is a valid token.
```
---
id: 393

Code snippet:
```
public String toXML(){
  StringBuilder stringBuilder=new StringBuilder();
  return stringBuilder.toString();
}
```
Comment:
```
Default toxml method to marshal object into xml.
```
---
id: 394

Code snippet:
```
public static String asHex(long value){
  return \"0x\" + Long.toHexString(value);
}
```
Comment:
```
Display as hex.
```
---
id: 395

Code snippet:
```
public Paragraph(String text){
  this(new Text(text));
}
```
Comment:
```
Creates a paragraph, initialized with a piece of text.
```
---
id: 396

Code snippet:
```
@Override public String toString(){
  StringBuilder b=new StringBuilder(64);
  b.append(\"name = \" + name + \" \");
  b.append(\"type = \" + type + \" \");
  b.append(\"reqTime = \" + reqTime + \" \");
  b.append(\"required = \" + required + \" \");
  b.append(\"fragment = \" + fragment + \" \");
  b.append(\"deferredValue = \" + deferredValue + \" \");
  b.append(\"expectedTypeName = \" + expectedTypeName + \" \");
  b.append(\"deferredMethod = \" + deferredMethod + \" \");
  b.append(\"methodSignature = \" + methodSignature);
  return b.toString();
}
```
Comment:
```
Returns a string representation of this tagattributeinfo, suitable for debugging purposes.
```
---
id: 397

Code snippet:
```
@Deprecated public boolean equals(String s){
  if (s == null || mimeType == null)   return false;
  return isMimeTypeEqual(s);
}
```
Comment:
```
Compares only the <code>mimetype</code> against the passed in <code>string</code> and <code>representationclass</code> is not considered in the comparison. if <code>representationclass</code> needs to be compared, then <code>equals(new dataflavor(s))</code> may be used.
```
---
id: 398

Code snippet:
```
public boolean isMember(SSOToken token) throws SSOException {
  return (SSOTokenManager.getInstance().isValidToken(token));
}
```
Comment:
```
Returns true if the given token is valid.
```
---
id: 399

Code snippet:
```
public void test_MultipleUpdatesInOneTables() throws SQLException {
  int id=1;
  String field=\"field3\";
  String selectQuery=\"SELECT * FROM \" + DatabaseCreator.TEST_TABLE1 + \" WHERE id=\"+ id;
  Statement statement=conn.createStatement();
  ResultSet result=statement.executeQuery(selectQuery);
  assertTrue(\"There is no records with id = \" + id,result.next());
  result.close();
  for (int i=0; i < numThreads; i++) {
    threadPool.runTask(createTask7(id,field));
  }
  threadPool.join();
  double expectedVal=id + numThreads;
  result=statement.executeQuery(selectQuery);
  assertTrue(\"There is no records with id = \" + id,result.next());
  result.close();
}
```
Comment:
```
This method is called when a statement has been created.
```
---
