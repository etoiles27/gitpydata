
    
    //window.addEventListener("popstate", popData, false);
    
    $(function(){
    	requestDefaultPage();
    });
    
    /*
    var viewState = false;
    function popData(event){
        
        var tempHash = location.hash;
        
        if (tempHash=="#eResult")
        {
            requestResultPage();
        } else {
            
        }
    }
    */
    
    function requestDefaultPage()
    {
        $(".customBackButton").hide();
        $.get("e2.html",function(result){
            $("#content").html(result);
        });
    }
    
    var resultValues = {};
    function requestResultPage()
    {
        $(".customBackButton").show();
        
        if (isNaN(parseInt($("#mi_weightc").val()))){
            requestDefaultPage();
            return;
        }
        
        cal();
        
        $.get("e1.html",function(result){
            $("#content").html(result);
            
            $("#aimi_t_result").append(resultStringFn());
            
            innerContent();
            window.scrollTo(0, 1);
        });
    }
    
   function innerContent()
        {
            if (resultValues.sex==1) {
                $("#content #aimi_sex").text("남자");
            } else {
                $("#content #aimi_sex").text("여자");
            }
            
            $("#content #aimi_height").text(resultValues.height);
            $("#content #aimi_weight").text(resultValues.weight);
            $("#content #aimi_age").text(resultValues.age);
            
            if (resultValues.act==1) {
                $("#content #aimi_act").text("심한 활동");
            } else if (resultValues.act==2) {
                $("#content #aimi_act").text("가벼운 활동");  
            } else if (resultValues.act==3) {
                $("#content #aimi_act").text("보통 활동"); 
            } else if (resultValues.act==4) {
                $("#content #aimi_act").text("가벼운 활동");
            } else if (resultValues.act==5) {
                $("#content #aimi_act").text("활동 안함");
            }
            
            $("#aimi_bmi").text(resultValues.bmi);
            $("#aimi_bmiResult").text(resultValues.bmiResult);
            $("#graph1_pt").css("left",resultValues.bmiX+"%");
            
            $("#aimi_tkcal").text(resultValues.bmrResult);
            $("#aimi_kcal1").text(resultValues.bmr);
            $("#aimi_kcal2").text(resultValues.digestion);
            $("#aimi_kcal3").text(resultValues.bmrActResult);
            
            $("#aimi_kcal1_width").css("width",resultValues.kcal1_width+"%");
            $("#aimi_kcal2_width").css("width",resultValues.kcal2_width+"%");
            $("#aimi_kcal3_width").css("width",resultValues.kcal3_width+"%");
            
            $("#raimi_weight").text(resultValues.weight);
            $("#raimi_bmi").text(resultValues.bmi);
            $("#raimi_bmiResult").text(resultValues.bmiResult);
            $("#raimi_kg1").text(resultValues.kg1);
            $("#raimi_kg2").text(resultValues.kg2);	
            $("#raimi_kg3").text(resultValues.kg3);
            
            $("#burnResult").text(resultValues.burnResult*-1);
            
            $("#fe").html(resultValues.s+":"+resultValues.e);
            
            
            
            $("#goal_date").text(resultValues.goal_date);
            $("#goal_burn").text(resultValues.goal_burn*-1);
            
            $("#goal_date1").text(resultValues.goal_date);
            $("#goal_burn1").text(resultValues.goal_burn*-1);
            
            $("#rs").text(resultValues.sResult);
            $("#re").text(resultValues.eResult);
            
            $("#rs1").text(resultValues.sResult);
            $("#rs2").text(resultValues.sResult);
            $("#re2").text(resultValues.bmrResult-resultValues.eResult);
            
            var _eResult = resultValues.bmrResult - resultValues.bmr;
            _eResult = 10-getRound( _eResult/resultValues.burnResult*10, 0);
            
            $("#slider_px1").css("left",_eResult*10+"%");
            
            oSlider.setValue(resultValues.s);
            
            if (resultValues.sex==1) {
            	$("#isGirl1").hide();
            	$("#isGirl2").hide();
            	$("#isGirl3").html("Kg입니다.");
            } else {
            	$("#isGirl3").html("Kg이고,");
            }
        }
        
        function resultStringFn()
        {
            var returnString = "";
            if (resultValues.bmiResult == "저체중") {
					returnString = "정상체중인데 체지방을 측정해보면 비만으로 결과가 나오는 분, 겉은 말라보이는데 밥을 조금만 먹어도 배가 불룩 나오는 복부비만인 분, 말라보이고 가벼워보이나 근육량이 너무 적어 기운이 없는 분, 체중조절을 오로지 다이어트(식사조절)로만 해왔던 분, 이런 분들이 보통 마른 비만입니다.  \
<br /><br /> \
마른 비만은 건강상 매우 안좋은 상태입니다. 지방간, 고지혈증 등 대사 증후군의 위험이 높으나 겉으로는 말라보이기에 방치하다가 병을 키우는 경우가 많습니다. 오랜 식사조절 다이어트로 근육량이 줄어든 것은 물론, 뼈의 밀도도 낮아 차후 골다공증에 걸리기도 쉽니다. 마른 비만인 분이 임신을 하거나 식사량이 늘게되면 아주 빠른 속도로 체중이 불어갑니다. 체중 증가 방지장치인 근육이 줄어 조금만 방심해도 체중이 빨리 늘게 되는 것이죠. \
<br /><br /> \
마른비만인 분들일수록 체중에 대해 민감합니다. 오히려 표준체중보다 저체중인데도 만족할 수가 없죠. 체중에 연연하기 보다는 전신을 골고루 움직여주는 운동을 해서 멋진 바디라인으로 다듬으면서 서서히 체성분의 변화를 꾀합니다. 운동과 영양섭취에 신경쓰면서 건강한 다이어트를 하면 몸의 체성분이 균형잡히게 발달하면서 오히려 체중이 늘 수는 있습니다. 근육이 성장해 체중은 늘지만 부피가크고 무게가 가벼운 체지방은 분해되어 싸이즈가 줄어듭니다. 그러기 위해서는 체중 보다는 체지방률에, 체중계 보다 체조성계의 말에 귀를 기울여야 합니다. 줄자로 싸이즈를 측정하거나 체지방의 변화를 기록하는 것이 바람직합니다. \
<br /><br /> \
마른 비만인 분들은 대다수 저칼로리 식이요법을 합니다. 그로인해 근손실을 초래하고 있으므로 단백질이 풍부한 식사를 해줘야 합니다. 또한 그간 저칼로리 다이어트로 식사량이 줄어 위, 소장, 대장 기능이 저하된 상태입니다. 조금씩 어려번 나눠 섭취하고 밥은 현미밥을, 찬으로 해초와 채소의 섭취를 늘립니다. 채소의 섭취가 늘면 배변이 활발해집니다. 식사량은 갑자기 늘리지 말고 차츰 늘려나갑니다. 마른 비만인 분들은 밥보다 빵을 좋아하는 경향이 있습니다. 빵도 나쁘진 않으나 가공이된 흰 밀가루에 소금을 버무리고 거기에 버터를 함께 배합해 구운 빵이 많습니다. 영양의 불균형을 초래하므로 밥으로 바꿔보시는 것이 좋겠습니다.";
					 	
        } else if (resultValues.bmiResult == "정상체중") {
					returnString = "정상체중이고, 정상 체성분률을 가지고 있다면 좋은 생활습관을 오래 유지하신 분일 것입니다. 특별히 살이 찌지도 않았는데도 꾸준히 운동과 식이요법을 하는 분들은 두가지 목적을 가진 분들일 것입니다. 첫째로 미용적인 측면에서의 몸관리를 하는 분들. 즉, 멋진 라인의 몸매, 멋진 가슴과 王자 복근으로 몸을 다듬기 위해 운동과 식사조절을 하는 분, 두 번째로 건강관리를 위해 꾸준히 운동하는 분. 즉, 생활의 활력, 성인병 예방, 노화방지와 장수를 위해 운동과 식사조절을 하는 분들입니다. \
<br /><br /> \
이런 분들은 체중과 건강을 오래 유지하는 것을 목표로 잡아야 합니다. 나이 25세가 지나면서 우리 몸의 근육량은 서서히 줄어들므로 걷기와 같은 유산소 운동만 하셔서는 안되고 적절한 양의 근력운동을 꼭 병행해줘야 합니다. 또한 유연성이 떨어질 우려가 있으니 요가, 기공 등 유연성과 파워를 함께 얻을 수 있는 운동을 함께 할 필요가 있습니다. 그리고 이런 운동들과 함께 건강한 식사습관을 생활화해야 합니다. 물론, 미용적인 측면에서 '과한'운동과 '과한'식사를하여 몸을 부풀리는 것은 자신의 취향입니다. \
<br /><br /> \
몸짱 만들기 원하는 분 : 자신의 목표에 맞는 웨이트 프로그램을 따라하면 됩니다. 시중에 다양한 웨이트 서적과 관련 사이트들을 이용하시면 됩니다. 혹은 카페의 데일리프로그램을 고중량으로 따라하시면 됩니다. 이 경우 필히 고단백 + 항산화 식단을 챙겨주셔야 합니다. \
<br /><br /> \
건강을 위해 운동하고자 하는 분 : 주 3~4일 하루 30분~1시간의 근력운동과 유산소 운동을 하고 틈나는대로 몸을 자주 움직이고 스트레칭도 자주 합니다. 요가, 기공, 걷기와 같은 생활속 운동을 주 운동으로 합니다. 그리고 규칙적인 식사, 과식을 하지 말고 단백질과 항산화 식단을 챙기시는게 좋습니다.";
			} else {
					returnString = "과체중이란 키에 비해 몸무게가 많이 나가는 경우입니다. 웨이트트레이닝을 오래 한 분이나 프로 운동선수들은 체구에 비해 체중이 많이 나갑니다. 그 이유는 근육이 많기 때문이죠. 그런 경우는 과체중이라 할 수 있어도 비만이라고 하지는 않습니다. 그러나, 근육이 적고 체지방이 많은 과체중의 경우 비만이라고 불리우죠. 대부분 운동을 게을리하는 분들의 경우 과체중이면 비만일 것입니다. 그러므로 체중계를 통한 비만도 검사보다 체조성계를 통한 비만도 검사를 추천합니다. \
<br /><br /> \
비만도가 그리 심하지 않은 중도비만은 가장 다이어트 욕구가 불탑니다. 조금만 노력하면 정상 체중이 될 수 있으니까요^^ 고도비만인 분은 체중이라도 줄였으면 좋겠다고 생각하지만 중도비만인 분들은 체중조절과 체형개선에 대한 욕구가 함께 있습니다. 고도비만의 경우와 마찬가지로 비만의 원인을 파악하고, 개선할 부분을 개선하고, 운동과 식사조절을 합시다. \
<br /><br /> \
비만이 심할수록 과식, 폭식을 하시는 분들이 많으며 오랜 나쁜 식습관으로 체내의 당대사가 나빠진 경우가 많습니다. 당대사가 불안정해지면 규칙적이고 정량의 식사를 하는 것이 더욱 힘듭니다. 그러므로 조금씩 자주 먹으며 위 크기를 줄이고 혈당을 안정시킬 필요가 있습니다. 배부르지 않을 정도로 세끼 식사를 챙겨 드시고, 식사 3시간 후 간단한 간식을 챙겨보세요. 허기가 덜 지고 저혈당 증세도 덜할꺼에요.";
            }
            return returnString;
        }
        
        function cal()
    		{
    			var div = parseInt( $(".mi_div:checked").val());
    			var weight = parseInt($("#mi_weightc").val());
				var height = parseInt($("#mi_heightc").val());
				var sex = parseInt( $(".mi_sex:checked").val());
				var age = parseInt( $("#mi_age").val());
				var goal_burn = parseInt( $("#mi_goal_burn").val());
				var goal_date = parseInt( $("#mi_goal_date").val());
				var s = parseInt( $("#mi_s").val());
				var e = parseInt( $("#mi_e").val());
				var act = parseInt( $(".mi_act:checked").val());
				
				resultValues.div = div;
				resultValues.weight = weight;
				resultValues.height = height;
				resultValues.sex = sex;
				resultValues.age = age;
				
				resultValues.goal_burn = weight-goal_burn;
				resultValues.goal_date = goal_date;
				resultValues.s = s;
				resultValues.e = e;
				resultValues.act = act;
				
				getBMI();
				getBMR();
				getBurn();
				getGoalResult();
				console.log(resultValues);
				
    		}
    		
    		var _0xfd7f=["\x73\x52\x65\x73\x75\x6C\x74","\x6C\x65\x6E\x67\x74\x68","\x77\x65\x69\x67\x68\x74","\x72\x20\x3A\x20","\x6C\x6F\x67","\x72\x31\x20\x3A\x20","\uBD84","\x68\x74\x6D\x6C","\x2E\x69\x63\x3A\x65\x71\x28","\x29","\x62\x75\x72\x6E\x52\x65\x73\x75\x6C\x74","\x73","\x65\x52\x65\x73\x75\x6C\x74","\x65","\x67\x6F\x61\x6C\x5F\x62\x75\x72\x6E","\x67\x6F\x61\x6C\x5F\x64\x61\x74\x65","\x64\x69\x76","\x73\x65\x78","\x62\x6D\x72","\x68\x65\x69\x67\x68\x74","\x61\x67\x65","\x61\x63\x74","\x62\x6D\x72\x41\x63\x74","\x62\x6D\x72\x41\x63\x74\x52\x65\x73\x75\x6C\x74","\x64\x69\x67\x65\x73\x74\x69\x6F\x6E","\x62\x6D\x72\x52\x65\x73\x75\x6C\x74","\x72\x6F\x75\x6E\x64","\x6B\x63\x61\x6C\x31\x5F\x77\x69\x64\x74\x68","\x6B\x63\x61\x6C\x32\x5F\x77\x69\x64\x74\x68","\x6B\x63\x61\x6C\x33\x5F\x77\x69\x64\x74\x68","\x6B\x67\x31","\x6B\x67\x32","\x6B\x67\x33","\x62\x69\x6D\x61\x6E\x64\x6F","\x62\x6D\x69","\x62\x6D\x69\x58","","\uC800\uCCB4\uC911","\uC815\uC0C1\uCCB4\uC911","\uACFC\uCCB4\uC911","\uACBD\uB3C4\uBE44\uB9CC","\uC911\uB4F1\uB3C4\uBE44\uB9CC","\x62\x6D\x69\x52\x65\x73\x75\x6C\x74"];function getKcalSport(){var _0xb2c8x2=resultValues[_0xfd7f[0]];var _0xb2c8x3=[1.0,1.3,1.5,1.8,2.0,3.0,3.5,4.3,6.0,6.5,7.0,9.8,6.5,8.0,7.0,7.5,2.5,2.3,4.0,6.0,2.3,2.5,3.3,4.0,3.0,3.5,4.3,8.0,5.0,7.8,8.8,12.3,5.5,7.8,7.8,7.3,10.0,4.8,6.0,9.8,4.8,7.0,9.8,14.0,7.0,10.0,12.0];for(var _0xb2c8x4=0;_0xb2c8x4<_0xb2c8x3[_0xfd7f[1]];_0xb2c8x4++){var _0xb2c8x5=resultValues[_0xfd7f[2]]*_0xb2c8x3[_0xb2c8x4]/60;if(_0xb2c8x4==7){console[_0xfd7f[4]](_0xfd7f[3]+_0xb2c8x5);c…





                
										var oSlider = new jindo.m.Slider('slider',{
                                            nMinValue : 0,
                                            nMaxValue : 10,
                                            nDefaultValue : 3
                                       }).attach({
                                           'beforeChange' : function(oCustomEvt){
                                               //반올림하여 정수로 값을 설정할때
                                               var nPos = Math.round(oCustomEvt.nValue);
                                               oCustomEvt.nAdjustValue = nPos;
                                               
                                               var _result = 10-nPos;
                                               $("#fe").html(nPos+":"+_result);
                                               
                                               resultValues.s = nPos;
                                               resultValues.e = _result;
                                               
                                               getGoalResult();
                                               
                                               $("#rs").text(resultValues.sResult);
                                               $("#re").text(resultValues.eResult);
                                               $("#goal_date").text(resultValues.goal_date);
                                               $("#goal_burn").text(resultValues.goal_burn);
           
                                               $("#rs1").text(resultValues.sResult);
                                               $("#rs2").text(resultValues.sResult);
                                               $("#re2").text( getRound( resultValues.bmrResult-resultValues.eResult, 1) );
                                               
                                               getKcalSport();
                                           }
                                       });
          
                                       